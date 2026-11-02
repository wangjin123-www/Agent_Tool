NXP Semiconductors 

# Chapter 44 Mode Entry Module (MC_ME) 

## 44.1 Chip-specific MC_ME information 

### 44.1.1 MC_ME modes 

This chip implements these modes: 

- Reset 

- Run 

- Standby 

The chip always enters Run mode after exiting Reset mode wherein you can configure the chip to perform its computational and communication functions. In Run mode: 

- The chip remains fully powered. The boot core is the only core enabled on Run entry. 

- You can enable and disable application cores and peripherals as needed, based on functional and power requirements. 

- You can configure the pins and self-test as needed. See "Self-Test programming sequence" section in the STCU2 chapter for the self-test programming sequence to be followed before initiating self-test, in which: 

   - Pins are safe-stated. 

   - No computational or communication activities are possible. 

- The chip automatically enters Reset mode after self-test (BIST) is complete. 

### 44.1.2 Core operation modes 

The Cortex-M7 cores in the chip support these two modes of operation: 

- Decoupled/independent operation 

- Coupled/lockstep operation 

The device configuration clients (utest_misc DCF client) control these modes of operation. See the DCF clients file attached to this document for details. 

### 44.1.3 MC_ME partition mapping of cores and peripherals 

MC_ME provides registers and interface signals to support multiple partitions. These MC_ME partitions are different from the chip's LBIST partitions described in the "Safety Overview" chapter. This chip has three MC_ME partitions: 

- Partition 0: Contains application cores and the on/off-platform slots on AIPS_0 bridge 

- Partition 1: Contains the on/off-platform slots on AIPS_1 bridge 

- Partition 2: Contains the on/off-platform slots on AIPS_2 bridge 

Table 225 and Table 226 specify the core and peripheral mapping on MC_ME partitions and their associated clock gating possiblities. 

MC_ME also provides provisions to control the booting address for application cores, which can be configured to start from a nondefault address location by appropriately configuring PRTNx_COREn_ADDR[ADDR]. 

### 44.1.4 Core clock gating 

MC_ME has individual core-clock enable fields that gate the application core clocks, which can also be clock gated by executing Waiting for Interrupt (WFI). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1441 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

You can enable the application cores by configuring the respective CCE fields. See Application core initialization process and Application core shutdown process for proper initialization and shutdown of application cores. There is no clock control for the HSE_B core. It needs to be only put into WFI if required to be shutdown (for example, in Standby mode). 

Table 225. MC_ME partition core mapping 

|Core|MC_ME partition|MC_ME clock enable register field|
|---|---|---|
|Cortex-M7_0|0|MC_ME.PRTN0_CORE0_PCONF[CCE]|
|Cortex-M7_1 (not present on S32K312 and S32K311)|0|MC_ME.PRTN0_CORE1_PCONF[CCE]|
|Cortex-M7_2 (Present on S32K358 only)|0|MC_ME.PRTN0_CORE2_PCONF[CCE]|



### 44.1.5 Peripheral clock gating 

See Peripheral initialization process and Peripheral shutdown process for proper initialization and shutdown of peripherals. See Table 226 for peripheral clock gating possibilities. 

The application core can program the reserved configurations. 

~~<mark>NOTE</mark>~~ 

Before accessing the registers of a peripheral to start using it, its clock must be turned on, otherwise, a Hard-Fault event will occur. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1442 / 4640 

Table 226. MC_ME partition peripheral mapping and clock control 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ0]|0|0|0|0|0|Yes|0|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ1]|1|1|0|0|0|Yes|1|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ2]|2|2|0|0|0|Yes|2|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ3]|3|3|0|0|0|Yes|3|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ4]|4|4|0|0|0|Yes|4|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ5]|5|5|0|0|0|Yes|5|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ6]|6|6|0|0|0|Yes|6|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ7]|7|7|0|0|0|Yes|7|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ8]|8|8|0|0|0|Yes|8|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ9]|9|9|0|0|0|Yes|9|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ10]|10|10|0|0|0|Yes|10|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ11]|11|11|0|0|0|Yes|11|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ12]|12|12|0|0|0|Yes|12|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ13]|13|13|0|0|0|Yes|13|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ14]|14|14|0|0|0|Yes|14|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ15]|15|15|0|0|0|Yes|15|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ16]|16|16|0|0|0|Yes|16|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ17]|17|17|0|0|0|Yes|17|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ18]|18|18|0|0|0|Yes|18|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ19]|19|19|0|0|0|Yes|19|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ20]|20|20|0|0|0|Yes|20|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ21]|21|21|0|0|0|Yes|21|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ22]|22|22|0|0|0|Yes|22|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ23]|23|23|0|0|0|Yes|23|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ24]|24|24|0|0|0|Yes|24|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ25]|25|25|0|0|0|Yes|25|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ26]|26|26|0|0|0|Yes|26|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ27]|27|27|0|0|0|Yes|27|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ28]|28|28|0|0|0|Yes|28|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ29]|29|29|0|0|0|Yes|29|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ30]|30|30|0|0|0|Yes|30|
|0|Reserved|PRTN0_COFB0_CLKEN[REQ31]|31|31|0|0|0|Yes|31|
|0|TRGMUX|PRTN0_COFB1_CLKEN[REQ32]|32|32|1|1|0|No|0|
|0|BCTU|PRTN0_COFB1_CLKEN[REQ33]|33|33|1|1|0|No|1|
|0|eMIOS_0|PRTN0_COFB1_CLKEN[REQ34]|34|34|1|1|0|No|2|
|0|eMIOS_1|PRTN0_COFB1_CLKEN[REQ35]|35|35|1|1|0|No|3|
|0|eMIOS_2|PRTN0_COFB1_CLKEN[REQ36]|36|36|1|1|0|No|4|
|0|Reserved|PRTN0_COFB1_CLKEN[REQ37]|37|37|0|0|0|No|5|
|0|LCU_0|PRTN0_COFB1_CLKEN[REQ38]|38|38|1|1|0|No|6|
|0|LCU_1|PRTN0_COFB1_CLKEN[REQ39]|39|39|1|1|0|No|7|
|0|ADC_0|PRTN0_COFB1_CLKEN[REQ40]|40|40|1|1|0|No|8|
|0|ADC_1|PRTN0_COFB1_CLKEN[REQ41]|41|41|1|1|0|No|9|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|0|ADC_2|PRTN0_COFB1_CLKEN[REQ42]|42|42|1|1|0|No|10|
|0|Reserved|PRTN0_COFB1_CLKEN[REQ43]|43|43|0|0|0|No|11|
|0|PIT_0|PRTN0_COFB1_CLKEN[REQ44]|44|44|1|1|1|No|12|
|0|PIT_1|PRTN0_COFB1_CLKEN[REQ45]|45|45|1|1|0|No|13|
|0|MU_A|PRTN0_COFB1_CLKEN[REQ46]|46|46|1|1|0|No|14|
|0|MU_B|PRTN0_COFB1_CLKEN[REQ47]|47|47|1|1|0|No|15|
|1|AXBS switch|PRTN1_COFB0_CLKEN[REQ0]|128|0|1|0|1|Yes|0|
|1|AXBS_0|PRTN1_COFB0_CLKEN[REQ1]|129|1|1|0|1|Yes|1|
|1|AXBS_1|PRTN1_COFB0_CLKEN[REQ2]|130|2|1|0|1|Yes|2|
|1|eDMA control and status<br>(MP_CSR; MP_ES;<br>MP_HRS)|PRTN1_COFB0_CLKEN[REQ3]|131|3|1|1|0|Yes|3|
|1|eDMA transfer control<br>descriptor 0|PRTN1_COFB0_CLKEN[REQ4]|132|4|1|1|0|Yes|4|
|1|eDMA transfer control<br>descriptor 1|PRTN1_COFB0_CLKEN[REQ5]|133|5|1|1|0|Yes|5|
|1|eDMA transfer control<br>descriptor 2|PRTN1_COFB0_CLKEN[REQ6]|134|6|1|1|0|Yes|6|
|1|eDMA transfer control<br>descriptor 3|PRTN1_COFB0_CLKEN[REQ7]|135|7|1|1|0|Yes|7|
|1|eDMA transfer control<br>descriptor 4|PRTN1_COFB0_CLKEN[REQ8]|136|8|1|1|0|Yes|8|
|1|eDMA transfer control<br>descriptor 5|PRTN1_COFB0_CLKEN[REQ9]|137|9|1|1|0|Yes|9|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|1|eDMA transfer control<br>descriptor 6|PRTN1_COFB0_CLKEN[REQ10]|138|10|1|1|0|Yes|10|
|1|eDMA transfer control<br>descriptor 7|PRTN1_COFB0_CLKEN[REQ11]|139|11|1|1|0|Yes|11|
|1|eDMA transfer control<br>descriptor 8|PRTN1_COFB0_CLKEN[REQ12]|140|12|1|1|0|Yes|12|
|1|eDMA transfer control<br>descriptor 9|PRTN1_COFB0_CLKEN[REQ13]|141|13|1|1|0|Yes|13|
|1|eDMA transfer control<br>descriptor 10|PRTN1_COFB0_CLKEN[REQ14]|142|14|1|1|0|Yes|14|
|1|eDMA transfer control<br>descriptor 11|PRTN1_COFB0_CLKEN[REQ15]|143|15|1|1|0|Yes|15|
|1|Debug APB page0|PRTN1_COFB0_CLKEN[REQ16]|144|16|1|0|1|Yes|16|
|1|Debug APB page1|PRTN1_COFB0_CLKEN[REQ17]|145|17|1|0|1|Yes|17|
|1|Debug APB page2|PRTN1_COFB0_CLKEN[REQ18]|146|18|1|0|1|Yes|18|
|1|Debug APB page3|PRTN1_COFB0_CLKEN[REQ19]|147|19|1|0|1|Yes|19|
|1|Debug APB paged area|PRTN1_COFB0_CLKEN[REQ20]|148|20|1|0|1|Yes|20|
|1|SDA_AP|PRTN1_COFB0_CLKEN[REQ21]|149|21|1|1|1|Yes|21|
|1|EIM|PRTN1_COFB0_CLKEN[REQ22]|150|22|1|1|0|Yes|22|
|1|ERM|PRTN1_COFB0_CLKEN[REQ23]|151|23|1|1|0|Yes|23|
|1|MSCM|PRTN1_COFB0_CLKEN[REQ24]|152|24|1|1|0|Yes|24|
|1|PRAMC_0|PRTN1_COFB0_CLKEN[REQ25]|153|25|1|0|1|Yes|25|
|1|Flash memory controller|PRTN1_COFB0_CLKEN[REQ26]|154|26|1|0|1|Yes|26|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|1|Flash memory controller<br>alternate|PRTN1_COFB0_CLKEN[REQ27]|155|27|1|0|1|Yes|27|
|1|SWT_0|PRTN1_COFB0_CLKEN[REQ28]|156|28|1|1|1|Yes|28|
|1|STM_0|PRTN1_COFB0_CLKEN[REQ29]|157|29|1|1|0|Yes|29|
|1|XRDC|PRTN1_COFB0_CLKEN[REQ30]|158|30|1|0|1|Yes|30|
|1|INTM|PRTN1_COFB0_CLKEN[REQ31]|159|31|1|1|0|Yes|31|
|1|DMAMUX_0|PRTN1_COFB1_CLKEN[REQ32]|160|32|1|1|0|No|0|
|1|DMAMUX_1|PRTN1_COFB1_CLKEN[REQ33]|161|33|1|1|0|No|1|
|1|RTC|PRTN1_COFB1_CLKEN[REQ34]|162|34|1|1|1|No|2|
|1|MC_RGM|PRTN1_COFB1_CLKEN[REQ35]|163|35|1|0|1|No|3|
|1|SIUL2_VIRTWRAPPER_<br>PDAC0|PRTN1_COFB1_CLKEN[REQ36]|164|36|1|0|1|No|4|
|1|SIUL2_VIRTWRAPPER_<br>PDAC0|PRTN1_COFB1_CLKEN[REQ37]|165|37|1|0|1|No|5|
|1|SIUL2_VIRTWRAPPER_<br>PDAC1|PRTN1_COFB1_CLKEN[REQ38]|166|38|1|0|1|No|6|
|1|SIUL2_VIRTWRAPPER_<br>PDAC1|PRTN1_COFB1_CLKEN[REQ39]|167|39|1|0|1|No|7|
|1|SIUL2_VIRTWRAPPER_<br>PDAC2|PRTN1_COFB1_CLKEN[REQ40]|168|40|1|0|1|No|8|
|1|SIUL2_VIRTWRAPPER_<br>PDAC2|PRTN1_COFB1_CLKEN[REQ41]|169|41|1|0|1|No|9|
|1|SIUL2_VIRTWRAPPER|PRTN1_COFB1_CLKEN[REQ42]|170|42|1|1|1|No|10|
|1|SSCM|PRTN1_COFB1_CLKEN[REQ43]|171|43|1|0|1|No|11|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|1|Reserved|PRTN1_COFB1_CLKEN[REQ44]|172|44|0|0|0|No|12|
|1|WKPU|PRTN1_COFB1_CLKEN[REQ45]|173|45|1|1|1|No|13|
|1|Reserved|PRTN1_COFB1_CLKEN[REQ46]|174|46|0|0|0|No|14|
|1|CMU 0-5|PRTN1_COFB1_CLKEN[REQ47]|175|47|1|1|0|No|15|
|1|Reserved|PRTN1_COFB1_CLKEN[REQ48]|176|48|0|0|0|No|16|
|1|TSPC|PRTN1_COFB1_CLKEN[REQ49]|177|49|1|1|1|No|17|
|1|32 kHz SIRC|PRTN1_COFB1_CLKEN[REQ50]|178|50|1|0|1|No|18|
|1|32 kHz SXOSC|PRTN1_COFB1_CLKEN[REQ51]|179|51|1|1|1|No|19|
|1|48 MHz FIRC|PRTN1_COFB1_CLKEN[REQ52]|180|52|1|0|1|No|20|
|1|8-40 MHz FXOSC|PRTN1_COFB1_CLKEN[REQ53]|181|53|1|1|1|No|21|
|1|MC_CGM|PRTN1_COFB1_CLKEN[REQ54]|182|54|1|0|1|No|22|
|1|MC_ME|PRTN1_COFB1_CLKEN[REQ55]|183|55|1|0|1|No|23|
|1|Frequency-modulated<br>PLL|PRTN1_COFB1_CLKEN[REQ56]|184|56|1|1|0|No|24|
|1|Reserved|PRTN1_COFB1_CLKEN[REQ57]|185|57|0|0|0|No|25|
|1|PMC|PRTN1_COFB1_CLKEN[REQ58]|186|58|1|0|1|No|26|
|1|Flash memory controller|PRTN1_COFB1_CLKEN[REQ59]|187|59|1|0|1|No|27|
|1|Flash memory controller<br>alternate|PRTN1_COFB1_CLKEN[REQ60]|188|60|1|0|1|No|28|
|1|Reserved|PRTN1_COFB1_CLKEN[REQ61]|189|61|0|0|0|No|29|
|1|Reserved|PRTN1_COFB1_CLKEN[REQ62]|190|62|0|0|0|No|30|
|1|PIT_2|PRTN1_COFB1_CLKEN[REQ63]|191|63|1|1|0|No|31|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|1|Reserved|PRTN1_COFB2_CLKEN[REQ64]|192|64|0|0|0|No|32|
|1|FlexCAN_0|PRTN1_COFB2_CLKEN[REQ65]|193|65|1|1|0|No|33|
|1|FlexCAN_1|PRTN1_COFB2_CLKEN[REQ66]|194|66|1|1|0|No|34|
|1|FlexCAN_2|PRTN1_COFB2_CLKEN[REQ67]|195|67|1|1|0|No|35|
|1|FlexCAN_3|PRTN1_COFB2_CLKEN[REQ68]|196|68|1|1|0|No|36|
|1|FlexCAN_4|PRTN1_COFB2_CLKEN[REQ69]|197|69|1|1|0|No|37|
|1|FlexCAN_5|PRTN1_COFB2_CLKEN[REQ70]|198|70|1|1|0|No|38|
|1|Reserved|PRTN1_COFB2_CLKEN[REQ71]|199|71|0|0|0|No|39|
|1|Reserved|PRTN1_COFB2_CLKEN[REQ72]|200|72|0|0|0|No|40|
|1|FlexIO|PRTN1_COFB2_CLKEN[REQ73]|201|73|1|1|0|No|41|
|1|LPUART_0|PRTN1_COFB2_CLKEN[REQ74]|202|74|1|1|0|No|42|
|1|LPUART_1|PRTN1_COFB2_CLKEN[REQ75]|203|75|1|1|0|No|43|
|1|LPUART_2|PRTN1_COFB2_CLKEN[REQ76]|204|76|1|1|0|No|44|
|1|LPUART_3|PRTN1_COFB2_CLKEN[REQ77]|205|77|1|1|0|No|45|
|1|LPUART_4|PRTN1_COFB2_CLKEN[REQ78]|206|78|1|1|0|No|46|
|1|LPUART_5|PRTN1_COFB2_CLKEN[REQ79]|207|79|1|1|0|No|47|
|1|LPUART_6|PRTN1_COFB2_CLKEN[REQ80]|208|80|1|1|0|No|48|
|1|LPUART_7|PRTN1_COFB2_CLKEN[REQ81]|209|81|1|1|0|No|49|
|1|Reserved|PRTN1_COFB2_CLKEN[REQ82]|210|82|0|0|0|No|50|
|1|Reserved|PRTN1_COFB2_CLKEN[REQ83]|211|83|0|0|0|No|51|
|1|LPI2C_0|PRTN1_COFB2_CLKEN[REQ84]|212|84|1|1|0|No|52|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|1|LPI2C_1|PRTN1_COFB2_CLKEN[REQ85]|213|85|1|1|0|No|53|
|1|LPSPI_0|PRTN1_COFB2_CLKEN[REQ86]|214|86|1|1|0|No|54|
|1|LPSPI_1|PRTN1_COFB2_CLKEN[REQ87]|215|87|1|1|0|No|55|
|1|LPSPI_2|PRTN1_COFB2_CLKEN[REQ88]|216|88|1|1|0|No|56|
|1|LPSPI_3|PRTN1_COFB2_CLKEN[REQ89]|217|89|1|1|0|No|57|
|1|Reserved|PRTN1_COFB2_CLKEN[REQ90]|218|90|0|0|0|No|58|
|1|SAI_0|PRTN1_COFB2_CLKEN[REQ91]|219|91|1|1|0|No|59|
|1|LPCMP_0|PRTN1_COFB2_CLKEN[REQ92]|220|92|1|1|1|No|60|
|1|LPCMP_1|PRTN1_COFB2_CLKEN[REQ93]|221|93|1|1|1|No|61|
|1|Reserved|PRTN1_COFB2_CLKEN[REQ94]|222|94|0|0|0|No|62|
|1|TempSense|PRTN1_COFB2_CLKEN[REQ95]|223|95|1|1|0|No|63|
|1|CRC|PRTN1_COFB3_CLKEN[REQ96]|224|96|1|1|0|No|64|
|1|FCCU (+FOSU)|PRTN1_COFB3_CLKEN[REQ97]|225|97|1|0|1|No|65|
|1|MTR|PRTN1_COFB3_CLKEN[REQ98]|226|98|1|0|1|No|66|
|1|HSE_MU0_B|PRTN1_COFB3_CLKEN[REQ99]|227|99|1|0|1|No|67|
|1|Reserved|PRTN1_COFB3_CLKEN[REQ100]|228|100|0|0|0|No|68|
|1|JDC|PRTN1_COFB3_CLKEN[REQ101]|229|101|1|0|1|No|69|
|1|Reserved|PRTN1_COFB3_CLKEN[REQ102]|230|102|1|1|1|No|70|
|1|Configuration GPR|PRTN1_COFB3_CLKEN[REQ103]|231|103|1|0|1|No|71|
|1|STCU2|PRTN1_COFB3_CLKEN[REQ104]|232|104|1|1|1|No|72|
|1|Reserved|PRTN1_COFB3_CLKEN[REQ105]|233|105|1|0|1|No|73|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|1|Reserved|PRTN1_COFB3_CLKEN[REQ106]|234|106|1|0|1|No|74|
|1|Reserved|PRTN1_COFB3_CLKEN[REQ107]|235|107|1|0|1|No|75|
|1|SELFTEST_GPR<sup>2</sup>|PRTN1_COFB3_CLKEN[REQ108]|236|108|1|0|1|No|76|
|1|Reserved|PRTN1_COFB3_CLKEN[REQ109]|237|109|0|0|0|No|77|
|1|Reserved|PRTN1_COFB3_CLKEN[REQ110]|238|110|1|0|1|No|78|
|2|XBIC (TCM backdoor<br>AHB_splitter)|PRTN2_COFB0_CLKEN[REQ0]|256|0|1|0|1|Yes|0|
|2|XBIC (eDMA AXBS-Lite)|PRTN2_COFB0_CLKEN[REQ1]|257|1|1|0|1|Yes|1|
|2|Reserved|PRTN2_COFB0_CLKEN[REQ2]|258|2|0|0|0|Yes|2|
|2|Reserved|PRTN2_COFB0_CLKEN[REQ3]|259|3|0|0|0|Yes|3|
|2|eDMA transfer control<br>descriptor 12|PRTN2_COFB0_CLKEN[REQ4]|260|4|1|1|0|Yes|4|
|2|eDMA transfer control<br>descriptor 13|PRTN2_COFB0_CLKEN[REQ5]|261|5|1|1|0|Yes|5|
|2|eDMA transfer control<br>descriptor 14|PRTN2_COFB0_CLKEN[REQ6]|262|6|1|1|0|Yes|6|
|2|eDMA transfer control<br>descriptor 15|PRTN2_COFB0_CLKEN[REQ7]|263|7|1|1|0|Yes|7|
|2|eDMA transfer control<br>descriptor 16|PRTN2_COFB0_CLKEN[REQ8]|264|8|1|1|0|Yes|8|
|2|eDMA transfer control<br>descriptor 17|PRTN2_COFB0_CLKEN[REQ9]|265|9|1|1|0|Yes|9|
|2|eDMA transfer control<br>descriptor 18|PRTN2_COFB0_CLKEN[REQ10]|266|10|1|1|0|Yes|10|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|S32K3xx Reference Manual, Rev. 4, 04/2022<br>Preliminary Information|
|---|



|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|2|eDMA transfer control<br>descriptor 19|PRTN2_COFB0_CLKEN[REQ11]|267|11|1|1|0|Yes|11|
|2|eDMA transfer control<br>descriptor 20|PRTN2_COFB0_CLKEN[REQ12]|268|12|1|1|0|Yes|12|
|2|eDMA transfer control<br>descriptor 21|PRTN2_COFB0_CLKEN[REQ13]|269|13|1|1|0|Yes|13|
|2|eDMA transfer control<br>descriptor 22|PRTN2_COFB0_CLKEN[REQ14]|270|14|1|1|0|Yes|14|
|2|eDMA transfer control<br>descriptor 23|PRTN2_COFB0_CLKEN[REQ15]|271|15|1|1|0|Yes|15|
|2|eDMA transfer control<br>descriptor 24|PRTN2_COFB0_CLKEN[REQ16]|272|16|1|1|0|Yes|16|
|2|eDMA transfer control<br>descriptor 25|PRTN2_COFB0_CLKEN[REQ17]|273|17|1|1|0|Yes|17|
|2|eDMA transfer control<br>descriptor 26|PRTN2_COFB0_CLKEN[REQ18]|274|18|1|1|0|Yes|18|
|2|eDMA transfer control<br>descriptor 27|PRTN2_COFB0_CLKEN[REQ19]|275|19|1|1|0|Yes|19|
|2|eDMA transfer control<br>descriptor 28|PRTN2_COFB0_CLKEN[REQ20]|276|20|1|1|0|Yes|20|
|2|eDMA transfer control<br>descriptor 29|PRTN2_COFB0_CLKEN[REQ21]|277|21|1|1|0|Yes|21|
|2|eDMA transfer control<br>descriptor 30|PRTN2_COFB0_CLKEN[REQ22]|278|22|1|1|0|Yes|22|
|2|eDMA transfer control<br>descriptor 31|PRTN2_COFB0_CLKEN[REQ23]|279|23|1|1|0|Yes|23|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|2|SEMA42|PRTN2_COFB0_CLKEN[REQ24]|280|24|1|1|0|Yes|24|
|2|PRAMC_1|PRTN2_COFB0_CLKEN[REQ25]|281|25|1|0|1|Yes|25|
|2|Reserved|PRTN2_COFB0_CLKEN[REQ26]|282|26|0|0|0|Yes|26|
|2|SWT_1|PRTN2_COFB0_CLKEN[REQ27]|283|27|1|1|0|Yes|27|
|2|Reserved|PRTN2_COFB0_CLKEN[REQ28]|284|28|0|0|0|Yes|28|
|2|STM_1|PRTN2_COFB0_CLKEN[REQ29]|285|29|1|1|0|Yes|29|
|2|Reserved|PRTN2_COFB0_CLKEN[REQ30]|286|30|0|0|0|Yes|30|
|2|Reserved|PRTN2_COFB0_CLKEN[REQ31]|287|31|0|0|0|Yes|31|
|2|EMAC|PRTN2_COFB1_CLKEN[REQ32]|288|32|1|1|0|No|0|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ33]|289|33|0|0|0|No|1|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ34]|290|34|0|0|0|No|2|
|2|LPUART_8|PRTN2_COFB1_CLKEN[REQ35]|291|35|1|1|0|No|3|
|2|LPUART_9|PRTN2_COFB1_CLKEN[REQ36]|292|36|1|1|0|No|4|
|2|LPUART_10|PRTN2_COFB1_CLKEN[REQ37]|293|37|1|1|0|No|5|
|2|LPUART_11|PRTN2_COFB1_CLKEN[REQ38]|294|38|1|1|0|No|6|
|2|LPUART_12|PRTN2_COFB1_CLKEN[REQ39]|295|39|1|1|0|No|7|
|2|LPUART_13|PRTN2_COFB1_CLKEN[REQ40]|296|40|1|1|0|No|8|
|2|LPUART_14|PRTN2_COFB1_CLKEN[REQ41]|297|41|1|1|0|No|9|
|2|LPUART_15|PRTN2_COFB1_CLKEN[REQ42]|298|42|1|1|0|No|10|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ43]|299|43|0|0|0|No|11|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ44]|300|44|0|0|0|No|12|



Table continues on the next page... 

Table 226. MC_ME partition peripheral mapping and clock control (continued) 

|AIPS<br>peripheral|Peripheral description<sup>1</sup>|MC_ME's PRTNn_COFBn_CLKEN<br>register fields|MC_ME<br>peripheral<br>control<br>register|MC_ME<br>peripheral<br>slot<br>number in<br>partition|MC_ME<br>COFB<br>present|MC_ME<br>CLKEN<br>present|MC_ME<br>default<br>CLKIN|On<br>platform|IPS slot<br>number|
|---|---|---|---|---|---|---|---|---|---|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ45]|301|45|0|0|0|No|13|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ46]|302|46|0|0|0|No|14|
|2|LPSPI_4|PRTN2_COFB1_CLKEN[REQ47]|303|47|1|1|0|No|15|
|2|LPSPI_5|PRTN2_COFB1_CLKEN[REQ48]|304|48|1|1|0|No|16|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ49]|305|49|0|0|0|No|17|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ50]|306|50|0|0|0|No|18|
|2|QuadSPI|PRTN2_COFB1_CLKEN[REQ51]|307|51|1|1|0|No|19|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ52]|308|52|0|0|0|No|20|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ53]|309|53|0|0|0|No|21|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ54]|310|54|0|0|0|No|22|
|2|SAI_1|PRTN2_COFB1_CLKEN[REQ55]|311|55|1|1|0|No|23|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ56]|312|56|0|0|0|No|24|
|2|Reserved|PRTN2_COFB1_CLKEN[REQ57]|313|57|0|0|0|No|25|
|2|LPCMP_2|PRTN2_COFB1_CLKEN[REQ58]|314|58|1|1|1|No|26|
|2|HSE_MU1_B|PRTN2_COFB1_CLKEN[REQ59]|315|59|1|0|1|No|27|
|2|CM7_0_TCM_CLKEN|PRTN2_COFB1_CLKEN[REQ62]|318|62|1|1|1|No|30|
|2|CM7_1_TCM_CLKEN|PRTN2_COFB1_CLKEN[REQ63]|319|63|1|1|1|No|31|



1. See the memory-map sheet attached to this document for details on available peripherals in different chips. 2. While accessing SELFTEST_GPR space, software must ensure that the STCU2 block has its clock enabled. i.e., MC_ME.PRTN1_COFB3_CLKEN[REQ104] configured as 1'b1. Not ensuring this might result in unpredictable device behaviour. 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.1.6 Application core initialization process 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1455-03.png)


<!-- Start of picture text -->
Start<br>Write the application core boot address to<br>PRTN   _CORE  _ADDR m n<br>Enable the application core clock by using<br>PRTN   _CORE  _PCONF[CCE] m n<br>Write to<br>PRTN   _CORE  _PUPD m n<br>Write valid key sequence to<br>CTL_KEY<br>Read the process-update status from<br>PRTN   _CORE  _PUPD m n<br>Process<br>completed<br>(PUPD=0)?<br>Read the application core clock status from<br>PRTN   _CORE  _STAT[CCS] m n<br>Core clock No<br>enabled? Run software diagnostics<br>Yes<br>Core starts execution<br>from boot address<br><!-- End of picture text -->

Figure 165. Application core initialization process 

### 44.1.7 Application core shutdown process 

If a debugger is attached to the chip and application debug is enabled, the application core continues running if you write 0 to MDM_AP.MDMAPCT[CM7_n_CORE_ACCESS]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1455 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1456-02.png)


<!-- Start of picture text -->
Core is in Running<br>or Active state<br>Stop any ongoing core<br>communication<br>Request core to enter WFI by writing<br>to corresponding core registers<br>Read the application core WFI status from<br>PRTN   _CORE  _STAT[WFI] m n<br>Disable the application core clock by using<br>PRTN   _CORE  _PCONF[CCE] m n<br>Write to<br>PRTN   _CORE  _PUPD m n<br>Write valid key sequence to<br>CTL_KEY<br>Read the process-update status from<br>PRTN   _CORE  _PUPD m n<br>Process<br>completed<br>(PUPD=0)?<br>Read the application core clock status by using<br>PRTN   _CORE  _STAT[CCS] m n<br>Core clock No<br>disabled? Run software diagnostics<br>Yes<br>Core in Turn-Off<br>or Inactive state<br>Figure 166. Application core shutdown process<br><!-- End of picture text -->

### 44.1.8 Peripheral initialization process 

You cannot control all the peripherals. For example, you cannot turn on and turn off the peripherals required for chip functionality across reset or power-up. They always remain on. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1456 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1457-02.png)


<!-- Start of picture text -->
Start<br>Consider the peripheral initialization<br>requirements or sequence in the<br>corresponding chapter<br>Enable the peripheral core clock by using<br>PRTN   _COFB  _CLKEN[REQ  ] m n z<br>Write to<br>PRTN   _PUPD m<br>Write valid key sequence to<br>CTL_KEY<br>Read the process-update status from<br>PRTN   _PUPD m<br>Process<br>completed<br>(PUPD=0)?<br>Read the application core clock status from<br>PRTN   _COFB  _STAT[BLOCK  ] m n z<br>Peripheral No<br>clock Run software diagnostics<br>enabled?<br>Yes<br>Start peripheral<br>operation<br>Figure 167. Peripheral initialization process<br><!-- End of picture text -->

### 44.1.9 Peripheral shutdown process 

You cannot control all the peripherals. For example, you cannot turn on and turn off the peripherals required for chip functionality across reset or power-up. They always remain on. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1457 / 4640 

NXP Semiconductors 

##### Mode Entry Module (MC_ME) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1458-02.png)


<!-- Start of picture text -->
Peripheral in Running<br>or Active state<br>Stop any ongoing communication with<br>input, output, cores or peripherals<br>Disable peripheral by writing to<br>its module-disable field (MDIS, EN or similar)<br>Read the peripheral status by reading back<br>the module-disable field (MDIS, EN or similar)<br>Disable the peripheral by using<br>PRTN   _COFB  _CLKEN[REQ  ] m n z<br>Write to<br>PRTN   _PUPD m<br>Write valid key sequence to<br>CTL_KEY<br>Read the process-update status from<br>PRTN   _PUPD m<br>Process<br>completed<br>(PUPD=0)?<br>Read the application core clock status from<br>PRTN   _COFB  _STAT[BLOCK  ] m n z<br>Peripheral No<br>clock Run software diagnostics<br>disabled?<br>Yes<br>Peripheral in Turn-Off<br>or Inactive state<br><!-- End of picture text -->

Figure 168. Peripheral shutdown process 

## 44.2 Introduction 

The MC_ME module generates control signals for a set of modules of the SoC. The set of signals are defined in corresponding 'Partition Configuration Registers'. It also implements a software-based mechanism for initiating a functional and destructive reset sequence and standby entry handshake with power management of SoC. See Figure 169 for the MC_ME block diagram. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1458 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1459-02.png)


<!-- Start of picture text -->
Configuration bus<br>Configuration registers<br>Partition 0 Partition 2 Mode controller<br>P P P P P P<br>Partition controls Partition controls<br><!-- End of picture text -->

Figure 169. MC_ME block diagram 

## 44.3 Features 

MC_ME includes the following features: 

- 3 logic partitions implementation and their controls 

- Core clock controls 

- Partition clock control 

- Control mechanism for initiating a destructive or functional reset sequence to MC_RGM 

- Control mechanism for initiating standby mode entry for SoC 

The logic partition inside MC_ME refers to a certain group of on-chip resources (or IP blocks) that are clubbed together to represent a single 'Partition' inside MC_ME. The MC_ME partition can be the same or different than an LBIST partition. Each of the MC_ME partitions implements a certain number of hardware processes. These hardware processes provide a mechanism to regulate various control signals provided to or received from the IP blocks. The corresponding status signals can also be monitored from MC_ME register(s). Each of the hardware processes is bound to finish in 512 cycles of the MC_ME register configuration clocks. Therefore, the hardware processes are non blocking in nature. Mismatch in the expected versus actual status of any hardware process is controlled by a pre-defined software. 

## 44.4 Partition processes 

Each of the processes inside the partition controls register space and corresponds to a control signal provided to that partition. A partition can include a core, or COFBs, or both. The MC_ME hardware processes provide control and status via signals provided to partitions. Each partition can be assigned a signal for control and a signal for status. Each of the control signals implements functionality for the partition. For example, clock gating and peripheral control. 

The hardware process can be triggered and monitored using a set of three registers: 

- Configuration register; for example, Partition n Process Configuration register 

- Update register; for example, Partition n Process Update register 

- Status register; for example, Partition n Status register 

Similar registers exist for cores inside the partition. 

The process setup and triggering procedure is shown in Figure 170. Each of the processes is independent of others and can be triggered or retriggered in parallel or sequential to other processes. The triggering or retriggering mechanism remains the same. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1459 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1460-02.png)


<!-- Start of picture text -->
Program<br>PRTNn_PCONF<br>register<br>Program<br>PRTNn_PUPD<br>register<br>Write valid key<br>sequence in<br>CTL_KEY register<br>Read<br>PRTNn_PUPD<br>register<br>Is<br>hardware N<br>update<br>process<br>finished?<br>Y<br>Is status N Run software<br>expected?<br>diagnostics<br>Y<br>Finish<br>Figure 170. Partition process setup procedure<br><!-- End of picture text -->

All the hardware processes are bound to finish in 512 cycles of the MC_ME configuration clock. If the actual and the expected status for a process does not match, then the diagnostics is left as a software responsibility. The software diagnostic can include further wait cycles for the status to match. 

## 44.5 Mode transition 

MC_ME implements a mode transition mechanism, whereby the mode of operation for SoC can be changed. Then module implements a mechanism that can lead to: 

- Destructive reset 

- Functional reset 

- Standby mode entry 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1460 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Destructive reset and functional reset requests from MC_ME are non-retractable transitions. After it is initiated, the other MC_ME functionality is rendered unusable and bus errors are provided for upcoming access to the MC_ME register until a reset sequence is executed by MC_RGM. Hence, it is vital that MC_RGM should never ignore or gate the reset requests from MC_ME. 

For transition into the standby mode, the software should ensure that required IP blocks such as clock sources and I/O communication are in their respective inactive states before initiating a standby mode transition to MC_ME. After MC_ME initiates a power down sequence request, it cannot be retracted. The SoC enters a standby power down sequence and then reenter power-up sequence even for cases where the standby wakeup happens right at the time of initiating a power-down sequence request. 

Steps for initiating the MC_ME mode transition: 

1. Setup the MODE_CONF register with the corresponding target mode bit set to logic-1. 

2. Perform the same update as done in the MODE_CONF register on the CONF_UPD register. 

3. Write the valid control key (0x5AF0) on the CTL_KEY register. 

4. Write the valid invert control key (0xA50F) on the CTL_KEY register. 

Mode transition to MC_ME is initiated, after the sequence mentioned above is completed. 

In step 1, if both FUNC_RST and DEST_RST in Mode Configuration Register (MODE_CONF) are 1: 

- After step 4 is complete, MC_ME initiates a mode transition to a destructive (not functional) reset. 

- After the chip exits reset, MC_RGM records that both MC_ME's destructive reset and MC_ME's functional reset were the reset source. 

~~<mark>NOTE</mark>~~ 

Any hardware partition processes setup, along with mode transition, is executed in parallel to the mode transition of MC_ME. 

## 44.6 Standby entry 

MC_ME provides hardware processes that implement shutdown sequencing of on-chip resources, such as cores and COFBs. The standby entry sequencing can be achieved or implemented using these hardware processes. The order of the hardware process is determined by the software and MC_ME. It requires no restriction in sequencing of the operation. Following is an example sequence for initiating a power-down sequence for entering the standby mode for SoC. The standby entry sequence should include (but not limited to) the following steps: 

1. Setting up wakeup lines 

2. Shutting down cores and COFBs 

3. Switching all MC_CGM muxes to FIRC with PCFS 

4. Powering down all clock sources except FIRC 

5. Setting up MC_ME using the main core and initiating a standby mode transition 

6. Executing WFI instruction on the main core (per Arm specification) 

### 44.6.1 Application core shutdown 

This section describes a mechanism for shutting down an application core. The sequence proposed here is extendible with the housekeeping tasks required for other IPs. Each of the tasks mentioned in the following sequence, can be further integrated with an SoC-specific task. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1461 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1462-02.png)


<!-- Start of picture text -->
MAIN CORE Application core MC_ME<br>Request application<br>cores to stop<br>Application cores<br>begin shut down<br>sequence<br>Disable all IRQs<br>undefined<br>Outstanding<br>delay instructions<br>finished/retired<br>WFI executed<br>MC_ME receives WFI<br>status<br>Check for application<br>MC_ME updates<br>core WFI status in<br>corresponding core<br>MC_ME status register<br>N WFI Y Application<br>received? core<br>shutdown<br>Figure 171. Application core shutdown<br><!-- End of picture text -->

After the application core is shutdown, the main core can optionally decide to gate the respective core clock using the corresponding core clock hardware process. 

### 44.6.2 Main core shutdown and standby entry 

This section describes standby entry sequence along with the main core shutdown. This sequence should only be initiated after SoC is ready for entering standby and has completed all the housekeeping activities. It is necessary that the main core has completed all the operations pertaining to other (application cores) and is the last active core before initiating the standby entry sequence. See Figure 172. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1462 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1463-02.png)


<!-- Start of picture text -->
Main core MC_ME MC_PCU<br>Program wakeup IP<br>Disable IRQs<br>and NMI<br>Program MC_ME for<br>valid main core ID<br>Finish outstanding<br>instructions<br>MC_ME waits for WFI<br>signaling from main<br>Program MC_ME for  core<br>standby mode<br>transition<br>Finish outstanding<br>instructions<br>WFI executed<br>Power down<br>sequence<br>initiated<br><!-- End of picture text -->

Figure 172. Standby entry sequence along with main core shutdown 

~~<mark>NOTE</mark>~~ 

- MC_ME initiates the power sequence to MC_PCU. This enables the main core to remain inactive (WFI state) until it is reset and power-up again at standby exit. 

## 44.7 MC_ME register descriptions 

MC_ME implements set hardware processes that can be used by the software for changing the mode of operation for a partition. Following are the features of MC_ME registers: 

- All registers are 32-bit wide. 

- Only 32-bit read and write accesses are supported. 

- Read/write accesses of less than 32 bits terminate with an error. 

- Writes to read-only register fields in writable registers are ignored and do not provide an error message. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1463 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

- Writes to read-only registers are aborted with an error message. 

### 44.7.1 MC_ME memory map 

MC_ME base address: 402D_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Control Key Register (CTL_KEY)|32|RW|0000_5AF0h|
|4h|Mode Configuration Register (MODE_CONF)|32|RW|0000_0000h|
|8h|Mode Update Register (MODE_UPD)|32|RW|0000_0000h|
|Ch|Mode Status Register (MODE_STAT)|32|RO|0000_0000h|
|10h|Main Core ID Register (MAIN_COREID)|32|RW|0000_0000h|
|100h|Partition 0 Process Configuration Register (PRTN0_PCONF)|32|RW|0000_0001h|
|104h|Partition 0 Process Update Register (PRTN0_PUPD)|32|RW|0000_0000h|
|108h|Partition 0 Status Register (PRTN0_STAT)|32|RO|0000_0001h|
|110h|Partition 0 COFB Set 0 Clock Status Register<br>(PRTN0_COFB0_STAT)|32|RO|0000_0000h|
|114h|Partition 0 COFB Set 1 Clock Status Register<br>(PRTN0_COFB1_STAT)|32|RO|0000_1000h|
|130h|Partition 0 COFB Set 0 Clock Enable Register<br>(PRTN0_COFB0_CLKEN)|32|RW|0000_0000h|
|134h|Partition 0 COFB Set 1 Clock Enable Register<br>(PRTN0_COFB1_CLKEN)|32|RW|0000_1000h|
|140h|Partition 0 Core 0 Process Configuration Register<br>(PRTN0_CORE0_PCONF)|32|RW|0000_0000h|
|144h|Partition 0 Core 0 Process Update Register (PRTN0_CORE0_PUPD)|32|RW|0000_0000h|
|148h|Partition 0 Core 0 Status Register (PRTN0_CORE0_STAT)|32|RO|0000_0000h|
|14Ch|Partition 0 Core 0 Address Register (PRTN0_CORE0_ADDR)|32|RW|0040_0000h|
|160h|Partition 0 Core 1 Process Configuration Register<br>(PRTN0_CORE1_PCONF)|32|RW|0000_0000h|
|164h|Partition 0 Core 1 Process Update Register (PRTN0_CORE1_PUPD)|32|RW|0000_0000h|
|168h|Partition 0 Core 1 Status Register (PRTN0_CORE1_STAT)|32|RO|0000_0000h|
|16Ch|Partition 0 Core 1 Address Register (PRTN0_CORE1_ADDR)|32|RW|0041_0000h|
|188h|Partition 0 Core 2 Status Register (PRTN0_CORE2_STAT)|32|RO|0000_0001h|
|18Ch|Partition 0 Core 2 Address Register (PRTN0_CORE2_ADDR)|32|RO|00BF_FC00h|
|1C0h|Partition 0 Core 4 Process Configuration Register<br>(PRTN0_CORE4_PCONF)|32|RW|0000_0000h|
|1C4h|Partition 0 Core 4 Process Update Register (PRTN0_CORE4_PUPD)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1464 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1C8h|Partition 0 Core 4 Status Register (PRTN0_CORE4_STAT)|32|RO|0000_0000h|
|1CCh|Partition 0 Core 4 Address Register (PRTN0_CORE4_ADDR)|32|RW|0042_0000h|
|300h|Partition 1 Process Configuration Register (PRTN1_PCONF)|32|RW|0000_0001h|
|304h|Partition 1 Process Update Register (PRTN1_PUPD)|32|RW|0000_0000h|
|308h|Partition 1 Status Register (PRTN1_STAT)|32|RO|0000_0001h|
|310h|Partition 1 COFB Set 0 Clock Status Register<br>(PRTN1_COFB0_STAT)|32|RO|5E3F_0007h|
|314h|Partition 1 COFB Set 1 Clock Status Register<br>(PRTN1_COFB1_STAT)|32|RO|7CFE_2FFCh|
|318h|Partition 1 COFB Set 2 Clock Status Register<br>(PRTN1_COFB2_STAT)|32|RO|3000_0000h|
|31Ch|Partition 1 COFB Set 3 Clock Status Register<br>(PRTN1_COFB3_STAT)|32|RO|0000_5FEEh|
|330h|Partition 1 COFB Set 0 Clock Enable Register<br>(PRTN1_COFB0_CLKEN)|32|RW|5E3F_0007h|
|334h|Partition 1 COFB Set 1 Clock Enable Register<br>(PRTN1_COFB1_CLKEN)|32|RW|7CFE_2FFCh|
|338h|Partition 1 COFB Set 2 Clock Enable Register<br>(PRTN1_COFB2_CLKEN)|32|RW|3000_0000h|
|33Ch|Partition 1 COFB Set 3 Clock Enable Register<br>(PRTN1_COFB3_CLKEN)|32|RW|0000_5FEEh|
|500h|Partition 2 Process Configuration Register (PRTN2_PCONF)|32|RW|0000_0001h|
|504h|Partition 2 Process Update Register (PRTN2_PUPD)|32|RW|0000_0000h|
|508h|Partition 2 Status Register (PRTN2_STAT)|32|RO|0000_0001h|
|510h|Partition 2 COFB Set 0 Clock Status Register<br>(PRTN2_COFB0_STAT)|32|RO|0600_0007h|
|514h|Partition 2 COFB Set 1 Clock Status Register<br>(PRTN2_COFB1_STAT)|32|RO|CC00_0000h|
|518h|Partition 2 COFB Set 2 Clock Status Register<br>(PRTN2_COFB2_STAT)|32|RO|0000_0001h|
|530h|Partition 2 COFB Set 0 Clock Enable Register<br>(PRTN2_COFB0_CLKEN)|32|RW|0600_0007h|
|534h|Partition 2 COFB Set 1 Clock Enable Register<br>(PRTN2_COFB1_CLKEN)|32|RW|CC00_0000h|
|538h|Partition 2 COFB Set 2 Clock Enable Register<br>(PRTN2_COFB2_CLKEN)|32|RW|0000_0001h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1465 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|



### 44.7.2 Control Key Register (CTL_KEY) 

#### Offset 

|Register|Offset|
|---|---|
|CTL_KEY|0h|



#### Function 

This register provides the mechanism to MC_ME for starting the hardware processes for the partition(s) and standby entry sequence. The hardware processes for partitions are triggered through the corresponding PRTNn_PCONF register. The mechanism to trigger the hardware processes of the respective partitions require two write operations: first time with key and second time with inverted key. The hexadecimal value of key is 0x5AF0 whereas for inverted key is 0xA50F. 

For initiating a standby entry sequence, the MODE_CONF register is used for providing a standby entry request along with a valid key combination. 

~~<mark>NOTE</mark>~~ Reads from this register return a valid key value to be written next. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1466-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>KEY<br>W<br>Reset 0 1 0 1 1 0 1 0 1 1 1 1 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—|This field is reserved and read returns zeros.|
|15-0|Control key|
|KEY|Key for starting the hardware processes. Writes with a value other than key or inverted key are ignored.<br>Reads return bit inverted value corresponding to last write.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1466 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.3 Mode Configuration Register (MODE_CONF) 

#### Offset 

|Register|Offset|
|---|---|
|MODE_CONF|4h|



#### Function 

This register is used for initiating a standby request or a reset event (destructive or functional) for the chip. The functional or destructive events are signaled to MC_RGM for further handling. 

~~<mark>NOTE</mark>~~ 

Software must not enable mode entry if the value of multiple fields is 1 in the MODE_CONF register. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1467-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R STAN 0 FUNC DEST_<br>W DBY  _RST  RST<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—|This field is reserved and read returns zeros.|
|15|Standby request|
|STANDBY|Writing a logic-1 to this bit along with the MODE_UPD register configuration and followed with a valid key<br>combination makes a standby entry sequence request to MC_ME.|
|14-2|Reserved|
|—|This field is reserved and read returns zeros.|
|1|Functional reset request|
|FUNC_RST|Writing a logic-1 to this bit along with the MODE_UPD register configuration and followed with a valid key<br>combination makes a functional reset event signaling to MC_RGM.|
|0|Destructive reset request|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1467 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|DEST_RST|Writing a logic-1 to this bit along with the MODE_UPD register configuration and followed with a valid key|
||combination makes a destructive reset event signaling to MC_RGM.|



### 44.7.4 Mode Update Register (MODE_UPD) 

#### Offset 

|Register|Offset|
|---|---|
|MODE_UPD|8h|



#### Function 

This register is used for initiating a mode change. Mode change refers to initiating a standby request, or generating a destructive or functional reset event to MC_RGM. Setting mode update field to logic-1, along with programming MODE_CONF registers and then followed by a valid key combination will generate a mode transition request. 

~~<mark>NOTE</mark>~~ 

The MODE_UPD register is implemented to make mode transition programming model the same as partition programming model. This is for future expansion inside MC_ME. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1468-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 MODE<br>W _UPD<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Mode update|
|MODE_UPD|Writing a logic-1 to this bit, followed by a valid key combination initiates a mode change as per the<br>MODE_CONF register.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1468 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.5 Mode Status Register (MODE_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|MODE_STAT|Ch|



#### Function 

This register provides the status of the previous mode. In case of standby exit, if the reset event status register of MC_RGM are set, then contents of this register should be ignored. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1469-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PREV_<br>R 0<br>MO...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Previous mode|
|PREV_MODE|This bit shows the status of the previous mode.|
||0b - The previous mode was reset (any reset).|
||1b - The previous mode was standby.|



### 44.7.6 Main Core ID Register (MAIN_COREID) 

#### Offset 

|Register|Offset|
|---|---|
|MAIN_COREID|10h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1469 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Function 

This register provides the ID of the main core sequencing the operation for the standby sequence. Core ID is required for entering in the standby mode, and using this MC_ME locates the WFI instruction execution of the main core. The core ID in this register is specified by the partition index along with the core index. 

~~<mark>NOTE</mark>~~ 

Before initiating a standby entry sequence, the contents of this register should point to the correct main core. Providing non-existing or incorrect core ID leads to unpredictable hardware behavior. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1470-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>PIDX  CIDX<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-13|Reserved|
|—|This field is reserved and read returns zeros.|
|12-8|Partition index|
|PIDX|Provides the partition index of the main core. Only values 0 - 2 can be written.|
|7-3|Reserved|
|—|This field is reserved and read returns zeros.|
|2-0|Core index|
|CIDX|Provides the core index of the main core inside the partition.|



### 44.7.7 Partition 0 Process Configuration Register (PRTN0_PCONF) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_PCONF|100h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1470 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Function 

This register provides a configuration for the hardware processes corresponding to partition 0. Each of the configuration bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding field in the PRTN0_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN0_PCONF and PRTN0_PUPD registers are used to determine the hardware processes to be executed. These are triggered in parallel and independent of each other. All dependent processes should be requested one after another from the software. 

~~<mark>NOTE</mark>~~ The partition clock enable/disable and output safe stating enable/disable are not standalone and must be done coherently in a fixed sequence. For details, see Software Reset Partition Turn-On Flow Chart and Software reset partition turn-off flowchart in Reset chapter. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1471-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0<br>PCE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-7|Reserved|
|—|This field is reserved and read returns zeros.|
|6|Reserved|
|—|This field is reserved and read returns zeros.|
|5|Reserved|
|—|This field is reserved and read returns zeros.|
|4|Reserved|
|—|This field is reserved and read returns zeros.|
|3|Reserved|
|—|This field is reserved and read returns zeros.|
|2|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1471 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Partition clock enable|
|PCE|This bit controls whether the clock to IPs (other than core(s)) in the partition should be enabled or disabled.|
||0b - Disable the clock to IPs|
||1b - Enable the clock to IPs|



### 44.7.8 Partition 0 Process Update Register (PRTN0_PUPD) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_PUPD|104h|



#### Function 

This register provides trigger signaling for the hardware processes corresponding to partition 0. Each of the control bit acts as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value in the corresponding bit field in the PRTN0_PCONF register. When the hardware process is finished the corresponding bit in this register is auto-cleared to logic-0. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1472-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0<br>PCUD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31-7|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1472 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|6|Reserved|
|—|This field is reserved and read returns zeros.|
|5|Reserved|
|—|This field is reserved and read returns zeros.|
|4|Reserved|
|—|This field is reserved and read returns zeros.|
|3|Reserved|
|—|This field is reserved and read returns zeros.|
|2|Reserved|
|—|This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0|Partition clock update|
|PCUD|This bit controls whether the hardware processes for enabling/disabling the clock to IPs (other than core(s))<br>in the partition should be triggered or not.<br>0b - Do not trigger the hardware process|
||1b - Trigger the hardware process|



### 44.7.9 Partition 0 Status Register (PRTN0_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_STAT|108h|



#### Function 

This register provides the current status of the control signals from the partition 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1473 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||0|0|0|0|0|0|PCS|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



#### Fields 

|Field|Function|
|---|---|
|31-7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>—|Reserved<br>This field is reserved and read returns zeros.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0|Partition clock status|
|PCS|This bit provides the status of the clock to partition.<br>0b - Clock is inactive|
||1b - Clock is active|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1474 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.10 Partition 0 COFB Set 0 Clock Status Register (PRTN0_COFB0_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_COFB0_STAT|110h|



#### Function 

This register provides the status of set 0 of COFBs inside partition 0. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 0. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1475-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>K3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30|Reserved|
|—|This field is reserved and read returns zeros.|
|29|Reserved|
|—|This field is reserved and read returns zeros.|
|28|Reserved|
|—|This field is reserved and read returns zeros.|
|27|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1475 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>—|Reserved<br>This field is reserved and read returns zeros.|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15<br>—|Reserved<br>This field is reserved and read returns zeros.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1476 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field<br>—|Function<br>This field is reserved and read returns zeros.|
|---|---|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10<br>—|Reserved<br>This field is reserved and read returns zeros.|
|9<br>—|Reserved<br>This field is reserved and read returns zeros.|
|8<br>—|Reserved<br>This field is reserved and read returns zeros.|
|7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>BLOCK3|IP block status<br>This bit provides the clock status of ERM1 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0|Reserved|
|—|This field is reserved and read returns zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1477 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.11 Partition 0 COFB Set 1 Clock Status Register (PRTN0_COFB1_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_COFB1_STAT|114h|



#### Function 

This register provides the status of set 1 of COFBs inside partition 0. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 0. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1478-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BLOC<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>K48<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0 0<br>K47  K46  K45  K44  K42  K41  K40  K39  K38  K36  K35  K34  K33  K32<br>W<br>Reset 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30|Reserved|
|—|This field is reserved and read returns zeros.|
|29|Reserved|
|—|This field is reserved and read returns zeros.|
|28|Reserved|
|—|This field is reserved and read returns zeros.|
|27|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1478 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>—|Reserved<br>This field is reserved and read returns zeros.|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>BLOCK48|IP block status<br>This bit provides the clock status of I3C_0 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|15<br>BLOCK47|IP block status<br>This bit provides the clock status of MU_2 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|14|IP block status<br>This bit provides the clock status of MU_2 in partition 0.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1479 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|BLOCK46|0b - Clock is not running.<br>1b - Clock is running.|
|13<br>BLOCK45|IP block status<br>This bit provides the clock status of PIT_1 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|12<br>BLOCK44|IP block status<br>This bit provides the clock status of PIT_0 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10|IP block status|
|BLOCK42|This bit provides the clock status of ADC_2 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|9|IP block status|
|BLOCK41|This bit provides the clock status of ADC_1 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|8|IP block status|
|BLOCK40|This bit provides the clock status of ADC_0 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|7|IP block status|
|BLOCK39|This bit provides the clock status of LCU_1 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|6|IP block status|
|BLOCK38|This bit provides the clock status of LCU_0 in partition 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1480 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is not running.<br>1b - Clock is running.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>BLOCK36|IP block status<br>This bit provides the clock status of eMIOS_2 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|3<br>BLOCK35|IP block status<br>This bit provides the clock status of eMIOS_1 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|2|IP block status|
|BLOCK34|This bit provides the clock status of eMIOS_0 in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|1<br>BLOCK33|IP block status<br>This bit provides the clock status of BCTU in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|
|0|IP block status|
|BLOCK32|This bit provides the clock status of TRGMUX in partition 0.<br>0b - Clock is not running.<br>1b - Clock is running.|



### 44.7.12 Partition 0 COFB Set 0 Clock Enable Register (PRTN0_COFB0_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_COFB0_CLKEN|130h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1481 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Function 

This register provides clock control signaling to the individual COFBs in set 0 inside partition 0. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1482-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>REQ3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1482 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15<br>—|Reserved<br>This field is reserved and read returns zeros.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1483 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|9<br>—|Reserved<br>This field is reserved and read returns zeros.|
|8<br>—|Reserved<br>This field is reserved and read returns zeros.|
|7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>REQ3|Clock enable<br>This bit provides the clock enable control for ERM1 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0<br>—|Reserved<br>This field is reserved and read returns zeros.|



### 44.7.13 Partition 0 COFB Set 1 Clock Enable Register (PRTN0_COFB1_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_COFB1_CLKEN|134h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1484 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Function 

This register provides clock control signaling to the individual COFBs in set 1 inside partition 0. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1485-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 REQ4<br>W 8<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R REQ4 REQ4 REQ4 REQ4 0 REQ4 REQ4 REQ4 REQ3 REQ3 0 REQ3 REQ3 REQ3 REQ3 REQ3<br>W 7  6  5  4  2  1  0  9  8  6  5  4  3  2<br>Reset 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1485 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>24<br>—|Function<br>Reserved<br>This field is reserved and read returns zeros.|
|---|---|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>REQ48|Clock enable<br>This bit provides the clock enable control for I3C_0 in partition 0.|
||0b - Clock is turned off.<br>1b - Clock is turned on.|
|15|Clock enable|
|REQ47|This bit provides the clock enable control for MU_2 in partition 0.<br>0b - Clock is turned off.|
||1b - Clock is turned on.|
|14|Clock enable|
|REQ46|This bit provides the clock enable control for MU_2 in partition 0.<br>0b - Clock is turned off.|
||1b - Clock is turned on.|
|13|Clock enable|
|REQ45|This bit provides the clock enable control for PIT_1 in partition 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1486 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is turned off.<br>1b - Clock is turned on.|
|12<br>REQ44|Clock enable<br>This bit provides the clock enable control for PIT_0 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10|Clock enable|
|REQ42|This bit provides the clock enable control for ADC_2 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|9|Clock enable|
|REQ41|This bit provides the clock enable control for ADC_1 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|8|Clock enable|
|REQ40|This bit provides the clock enable control for ADC_0 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|7|Clock enable|
|REQ39|This bit provides the clock enable control for LCU_1 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|6|Clock enable|
|REQ38|This bit provides the clock enable control for LCU_0 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4|Clock enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1487 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|REQ36|This bit provides the clock enable control for eMIOS_2 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|3<br>REQ35|Clock enable<br>This bit provides the clock enable control for eMIOS_1 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|2<br>REQ34|Clock enable<br>This bit provides the clock enable control for eMIOS_0 in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|1<br>REQ33|Clock enable<br>This bit provides the clock enable control for BCTU in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|0|Clock enable|
|REQ32|This bit provides the clock enable control for TRGMUX in partition 0.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|



### 44.7.14 Partition 0 Core 0 Process Configuration Register (PRTN0_CORE0_PCONF) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE0_PCONF|140h|



#### Function 

This register provides configurations for the Core 0 hardware processes corresponding to partition 0. Each of the configuration bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding field in the PRTN0_CORE0_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN0_CORE0_PUPD and PRTN0_CORE0_PCONF registers are used to determine the hardware processes to be executed. These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one after another from the software. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1488 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1489-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>CCE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 0 clock enable|
|CCE|This bit controls whether the clock to Core 0 in partition 0 should be enabled or disabled.|
||0b - Disable the core clock|
||1b - Enable the core clock|



### 44.7.15 Partition 0 Core 0 Process Update Register (PRTN0_CORE0_PUPD) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE0_PUPD|144h|



#### Function 

This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value in the corresponding bit field in the PRTN0_CORE0_PCONF register. When the hardware process is finished, the corresponding bit in this register is auto-cleared to logic-0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1489 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||CCUP|
|W||||||||||||||||D|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 0 clock update|
|CCUPD|This bit controls whether the hardware processes for enabling/disabling the clock to Core 0 in the partition<br>0 should be triggered or not.|
||0b - Do not trigger the hardware process|
||1b - Trigger the hardware process|



### 44.7.16 Partition 0 Core 0 Status Register (PRTN0_CORE0_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE0_STAT|148h|



#### Function 

This register provides the status corresponding to Core 0 in partition 0. The status signal corresponds to clock states and the WFI signal included from Core 0. 

~~<mark>NOTE</mark>~~ 

The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power mode). So, simple reset read sweep will always return current value (different than other register reads such as on control registers). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1490 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|WFI||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||CCS|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|Wait for interrupt status|
|WFI|This bit provides the WFI status approaching from Core 0 in partition 0.<br>0b - No WFI executed|
||1b - WFI executed|
|30-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 0 clock process status|
|CCS|This bit provides the status of the clock corresponding to core clock enablement/disablement.<br>0b - Clock is inactive.<br>1b - Clock is active.|



### 44.7.17 Partition 0 Core 0 Address Register (PRTN0_CORE0_ADDR) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE0_ADDR|14Ch|



#### Function 

This register contains the boot address for Core 0 in partition 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1491 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1492-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-2|Address|
|ADDR|Core 0 boot address|
|1-0|Reserved|
|—|This field is reserved and read returns zeros.|



### 44.7.18 Partition 0 Core 1 Process Configuration Register (PRTN0_CORE1_PCONF) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE1_PCONF|160h|



#### Function 

This register provides configurations for the Core 1 hardware processes corresponding to partition 0. Each of the configuration bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding field in the PRTN0_CORE1_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN0_CORE1_PUPD and PRTN0_CORE1_PCONF registers are used to determine the hardware processes to be executed. These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one after another from the software. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1492 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1493-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>CCE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 1 clock enable|
|CCE|This bit controls whether the clock to Core 1 in partition 0 should be enabled or disabled.|
||0b - Disable the core clock|
||1b - Enable the core clock|



### 44.7.19 Partition 0 Core 1 Process Update Register (PRTN0_CORE1_PUPD) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE1_PUPD|164h|



#### Function 

This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value in the corresponding bit field in the PRTN0_CORE1_PCONF register. When the hardware process is finished, the corresponding bit in this register is auto-cleared to logic-0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1493 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||CCUP|
|W||||||||||||||||D|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 1 clock update|
|CCUPD|This bit controls whether the hardware processes for enabling/disabling the clock to Core 1 in the partition<br>0 should be triggered or not.|
||0b - Do not trigger the hardware process|
||1b - Trigger the hardware process|



### 44.7.20 Partition 0 Core 1 Status Register (PRTN0_CORE1_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE1_STAT|168h|



#### Function 

This register provides the status corresponding to Core 1 in partition 0. The status signal corresponds to clock states and the WFI signal included from Core 1. 

~~<mark>NOTE</mark>~~ 

The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power mode). So, simple reset read sweep will always return current value (different than other register reads such as on control registers). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1494 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|WFI||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||CCS|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|Wait for interrupt status|
|WFI|This bit provides the WFI status approaching from Core 1 in partition 0.<br>0b - No WFI executed|
||1b - WFI executed|
|30-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 1 clock process status|
|CCS|This bit provides the status of the clock corresponding to core clock enablement/disablement.<br>0b - Clock is inactive.<br>1b - Clock is active.|



### 44.7.21 Partition 0 Core 1 Address Register (PRTN0_CORE1_ADDR) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE1_ADDR|16Ch|



#### Function 

This register contains the boot address for Core 1 in partition 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1495 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1496-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-2|Address|
|ADDR|Core 1 boot address|
|1-0|Reserved|
|—|This field is reserved and read returns zeros.|



### 44.7.22 Partition 0 Core 2 Status Register (PRTN0_CORE2_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE2_STAT|188h|



#### Function 

This register provides the status corresponding to Core 2 in partition 0. The status signal corresponds to clock states and the WFI signal included from Core 2. 

|~~NOTE~~|
|---|



The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power mode). So, simple reset read sweep will always return current value (different than other register reads such as on control registers). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1496 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|WFI||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||CCS|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



#### Fields 

|Field|Function|
|---|---|
|31|Wait for interrupt status|
|WFI|This bit provides the WFI status approaching from Core 2 in partition 0.|
||0b - No WFI executed|
||1b - WFI executed|
|30-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 2 clock process status|
|CCS|This bit provides the status of the clock corresponding to core clock enablement/disablement.|
||1b - Clock is active.|



### 44.7.23 Partition 0 Core 2 Address Register (PRTN0_CORE2_ADDR) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE2_ADDR|18Ch|



#### Function 

This register contains the boot address for Core 2 in partition 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1497 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1498-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R ADDR  0<br>W<br>Reset 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-2|Address|
|ADDR|Core 2 boot address|
|1-0|Reserved|
|—|This field is reserved and read returns zeros.|



### 44.7.24 Partition 0 Core 4 Process Configuration Register (PRTN0_CORE4_PCONF) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE4_PCONF|1C0h|



#### Function 

This register provides configurations for the Core 4 hardware processes corresponding to partition 0. Each of the configuration bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding field in the PRTN0_CORE4_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN0_CORE4_PUPD and PRTN0_CORE4_PCONF registers are used to determine the hardware processes to be executed. These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one after another from the software. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1498 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1499-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>CCE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 4 clock enable|
|CCE|This bit controls whether the clock to Core 4 in partition 0 should be enabled or disabled.|
||0b - Disable the core clock|
||1b - Enable the core clock|



### 44.7.25 Partition 0 Core 4 Process Update Register (PRTN0_CORE4_PUPD) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE4_PUPD|1C4h|



#### Function 

This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value in the corresponding bit field in the PRTN0_CORE4_PCONF register. When the hardware process is finished, the corresponding bit in this register is auto-cleared to logic-0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1499 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1500-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CCUP<br>D<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 4 clock update|
|CCUPD|This bit controls whether the hardware processes for enabling/disabling the clock to Core 4 in the partition<br>0 should be triggered or not.|
||0b - Do not trigger the hardware process|
||1b - Trigger the hardware process|



### 44.7.26 Partition 0 Core 4 Status Register (PRTN0_CORE4_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE4_STAT|1C8h|



#### Function 

This register provides the status corresponding to Core 4 in partition 0. The status signal corresponds to clock states and the WFI signal included from Core 4. 

~~<mark>NOTE</mark>~~ 

The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power mode). So, simple reset read sweep will always return current value (different than other register reads such as on control registers). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1500 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|WFI||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||CCS|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|Wait for interrupt status|
|WFI|This bit provides the WFI status approaching from Core 4 in partition 0.<br>0b - No WFI executed|
||1b - WFI executed|
|30-1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Core 4 clock process status|
|CCS|This bit provides the status of the clock corresponding to core clock enablement/disablement.<br>0b - Clock is inactive.<br>1b - Clock is active.|



### 44.7.27 Partition 0 Core 4 Address Register (PRTN0_CORE4_ADDR) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN0_CORE4_ADDR|1CCh|



#### Function 

This register contains the boot address for Core 4 in partition 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1501 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1502-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-2|Address|
|ADDR|Core 4 boot address|
|1-0|Reserved|
|—|This field is reserved and read returns zeros.|



### 44.7.28 Partition 1 Process Configuration Register (PRTN1_PCONF) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_PCONF|300h|



#### Function 

This register provides a configuration for the hardware processes corresponding to partition 1. Each of the configuration bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding field in the PRTN1_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN1_PCONF and PRTN1_PUPD registers are used to determine the hardware processes to be executed. These are triggered in parallel and independent of each other. All dependent processes should be requested one after another from the software. 

~~<mark>NOTE</mark>~~ 

The partition clock enable/disable and output safe stating enable/disable are not standalone and must be done coherently in a fixed sequence. For details, see Software Reset Partition Turn-On Flow Chart and Software reset partition turn-off flowchart in Reset chapter. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1502 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||0|0|0|0|0|0|PCE|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



#### Fields 

|Field|Function|
|---|---|
|31-7|Reserved|
|—|This field is reserved and read returns zeros.|
|6|Reserved|
|—|This field is reserved and read returns zeros.|
|5|Reserved|
|—|This field is reserved and read returns zeros.|
|4|Reserved|
|—|This field is reserved and read returns zeros.|
|3|Reserved|
|—|This field is reserved and read returns zeros.|
|2|Reserved|
|—|This field is reserved and read returns zeros.|
|1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Partition clock enable|
|PCE|This bit controls whether the clock to IPs (other than core(s)) in the partition should be enabled or disabled.<br>0b - Disable the clock to IPs|
||1b - Enable the clock to IPs|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1503 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.29 Partition 1 Process Update Register (PRTN1_PUPD) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_PUPD|304h|



#### Function 

This register provides trigger signaling for the hardware processes corresponding to partition 1. Each of the control bit acts as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value in the corresponding bit field in the PRTN1_PCONF register. When the hardware process is finished the corresponding bit in this register is auto-cleared to logic-0. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1504-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0<br>PCUD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-7|Reserved|
|—|This field is reserved and read returns zeros.|
|6|Reserved|
|—|This field is reserved and read returns zeros.|
|5|Reserved|
|—|This field is reserved and read returns zeros.|
|4|Reserved|
|—|This field is reserved and read returns zeros.|
|3|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1504 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|2|Reserved|
|—|This field is reserved and read returns zeros.|
|1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Partition clock update|
|PCUD|This bit controls whether the hardware processes for enabling/disabling the clock to IPs (other than core(s))<br>in the partition should be triggered or not.|
||0b - Do not trigger the hardware process|
||1b - Trigger the hardware process|



### 44.7.30 Partition 1 Status Register (PRTN1_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_STAT|308h|



#### Function 

This register provides the current status of the control signals from the partition 1. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1505-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0 PCS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

#### Fields 

|Field|Function||
|---|---|---|
|31-7|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1505 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>—|Reserved<br>This field is reserved and read returns zeros.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0|Partition clock status|
|PCS|This bit provides the status of the clock to partition.<br>0b - Clock is inactive|
||1b - Clock is active|



### 44.7.31 Partition 1 COFB Set 0 Clock Status Register (PRTN1_COFB0_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB0_STAT|310h|



#### Function 

This register provides the status of set 0 of COFBs inside partition 1. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1506 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1507-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0<br>K31  K30  K29  K28  K27  K26  K25  K24  K23  K21  K20  K19  K18  K17  K16<br>W<br>Reset 0 1 0 1 1 1 1 0 0 0 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R<br>K15  K14  K13  K12  K11  K10  K9  K8  K7  K6  K5  K4  K3  K2  K1  K0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>BLOCK31|IP block status<br>This bit provides the clock status of INTM in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|30<br>BLOCK30|IP block status<br>This bit provides the clock status of XRDC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|29<br>BLOCK29|IP block status<br>This bit provides the clock status of STM 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|28<br>BLOCK28|IP block status<br>This bit provides the clock status of SWT 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|27<br>BLOCK27|IP block status<br>This bit provides the clock status of PFC alt in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|26|IP block status<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1507 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|BLOCK26|This bit provides the clock status of PFC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|25<br>BLOCK25|IP block status<br>This bit provides the clock status of PRAM 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|24<br>BLOCK24|IP block status<br>This bit provides the clock status of MSCM in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|23<br>BLOCK23|IP block status<br>This bit provides the clock status of block 23 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>BLOCK21|IP block status<br>This bit provides the clock status of SDA-AP in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|20<br>BLOCK20|IP block status<br>This bit provides the clock status of Debug APB Paged Area in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|19<br>BLOCK19|IP block status<br>This bit provides the clock status of Debug APB Page3 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|18|IP block status|
|BLOCK18|This bit provides the clock status of Debug APB Page2 in partition 1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1508 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is not running.<br>1b - Clock is running.|
|17<br>BLOCK17|IP block status<br>This bit provides the clock status of Debug APB Page1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|16|IP block status|
|BLOCK16|This bit provides the clock status of Debug APB Page0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|15<br>BLOCK15|IP block status<br>This bit provides the clock status of eDMA TCD 11 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|14<br>BLOCK14|IP block status<br>This bit provides the clock status of eDMA TCD 10 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|13<br>BLOCK13|IP block status<br>This bit provides the clock status of eDMA TCD 9 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|12<br>BLOCK12|IP block status<br>This bit provides the clock status of eDMA TCD 8 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|11<br>BLOCK11|IP block status<br>This bit provides the clock status of eDMA TCD7 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|10|IP block status<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1509 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|BLOCK10|This bit provides the clock status of eDMA TCD 6 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|9<br>BLOCK9|IP block status<br>This bit provides the clock status of eDMA TCD 5 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|8<br>BLOCK8|IP block status<br>This bit provides the clock status of eDMA TCD 4 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|7<br>BLOCK7|IP block status<br>This bit provides the clock status of eDMA TCD 3 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|6<br>BLOCK6|IP block status<br>This bit provides the clock status of eDMA TCD 2 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|5<br>BLOCK5|IP block status<br>This bit provides the clock status of eDMA TCD 1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|4<br>BLOCK4|IP block status<br>This bit provides the clock status of eDMA in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|3<br>BLOCK3|IP block status<br>This bit provides the clock status of eDMA in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1510 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|2|IP block status|
|BLOCK2|This bit provides the clock status of Periph_XBIC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|1|IP block status|
|BLOCK1|This bit provides the clock status of System_XBIC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|0|IP block status|
|BLOCK0|This bit provides the clock status of AXBS in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|



### 44.7.32 Partition 1 COFB Set 1 Clock Status Register (PRTN1_COFB1_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB1_STAT|314h|



#### Function 

This register provides the status of set 1 of COFBs inside partition 1. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 1. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1511-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0<br>K63  K62  K61  K60  K59  K58  K57  K56  K55  K54  K53  K52  K51  K50  K49<br>W<br>Reset 0 1 1 1 1 1 0 0 1 1 1 1 1 1 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0 0<br>K47  K45  K43  K42  K41  K40  K39  K38  K37  K36  K35  K34  K33  K32<br>W<br>Reset 0 0 1 0 1 1 1 1 1 1 1 1 1 1 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1511 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Fields 

|Field<br>31<br>BLOCK63|Function<br>IP block status<br>This bit provides the clock status of PIT 2 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|---|---|
|30<br>BLOCK62|IP block status<br>This bit provides the clock status of block 62 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|29|IP block status|
|BLOCK61|This bit provides the clock status of block 61 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|28<br>BLOCK60|IP block status<br>This bit provides the clock status of FMU_alt in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|27|IP block status|
|BLOCK59|This bit provides the clock status of FMU in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|26<br>BLOCK58|IP block status<br>This bit provides the clock status of PMC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|25|IP block status|
|BLOCK57|This bit provides the clock status of PLL 2 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|24|IP block status|
|BLOCK56|This bit provides the clock status of PLL in partition 1.<br>0b - Clock is not running.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1512 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function<br>1b - Clock is running.|
|---|---|
|23<br>BLOCK55|IP block status<br>This bit provides the clock status of MC_ME in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|22<br>BLOCK54|IP block status<br>This bit provides the clock status of MC_CGM in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|21<br>BLOCK53|IP block status<br>This bit provides the clock status of FXOSC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|20<br>BLOCK52|IP block status<br>This bit provides the clock status of FIRC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|19<br>BLOCK51|IP block status<br>This bit provides the clock status of SXOSC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|18<br>BLOCK50|IP block status<br>This bit provides the clock status of SIRC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|17<br>BLOCK49|IP block status<br>This bit provides the clock status of TSPC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1513 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|15|IP block status|
|BLOCK47|This bit provides the clock status of CMU_0-5 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>BLOCK45|IP block status<br>This bit provides the clock status of WKPU in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>BLOCK43|IP block status<br>This bit provides the clock status of DCM in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|10<br>BLOCK42|IP block status<br>This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC3 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|9<br>BLOCK41|IP block status<br>This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC2_M7_1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|8<br>BLOCK40|IP block status<br>This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC2_M7_1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|7|IP block status|
|BLOCK39|This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC1_M7_0 in partition 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1514 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is not running.<br>1b - Clock is running.|
|6<br>BLOCK38|IP block status<br>This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC1_M7_0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|5<br>BLOCK37|IP block status<br>This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC0_HSE in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|4|IP block status|
|BLOCK36|This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC0_HSE in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|3|IP block status|
|BLOCK35|This bit provides the clock status of MC_RGM in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|2|IP block status|
|BLOCK34|This bit provides the clock status of RTC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|1|IP block status|
|BLOCK33|This bit provides the clock status of DMAMUX 1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|0|IP block status|
|BLOCK32|This bit provides the clock status of DMAMUX 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1515 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.33 Partition 1 COFB Set 2 Clock Status Register (PRTN1_COFB2_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB2_STAT|318h|



#### Function 

This register provides the status of set 2 of COFBs inside partition 1. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 1. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1516-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0 0 0 0<br>K95  K93  K92  K91  K89  K88  K87  K86  K85  K84  K81  K80<br>W<br>Reset 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0<br>K79  K78  K77  K76  K75  K74  K73  K72  K71  K70  K69  K68  K67  K66  K65<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|IP block status|
|BLOCK95|This bit provides the clock status of TMU in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|30|Reserved|
|—|This field is reserved and read returns zeros.|
|29|IP block status|
|BLOCK93|This bit provides the clock status of LPCMP 1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1516 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>28|Function<br>IP block status|
|---|---|
|BLOCK92|This bit provides the clock status of LPCMP 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|27<br>BLOCK91|IP block status<br>This bit provides the clock status of SAI_0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>BLOCK89|IP block status<br>This bit provides the clock status of LPSPI 3 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|24<br>BLOCK88|IP block status<br>This bit provides the clock status of LPSPI 2 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|23<br>BLOCK87|IP block status<br>This bit provides the clock status of LPSPI 1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|22<br>BLOCK86|IP block status<br>This bit provides the clock status of LPSPI 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|21<br>BLOCK85|IP block status<br>This bit provides the clock status of LPI2C 1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|20|IP block status<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1517 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|BLOCK84|This bit provides the clock status of LPI2C 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17|IP block status|
|BLOCK81|This bit provides the clock status of LPUART 7 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|16|IP block status|
|BLOCK80|This bit provides the clock status of LPUART 6 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|15|IP block status|
|BLOCK79|This bit provides the clock status of LPUART 5 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|14<br>BLOCK78|IP block status<br>This bit provides the clock status of LPUART 4 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|13|IP block status|
|BLOCK77|This bit provides the clock status of LPUART 3 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|12|IP block status|
|BLOCK76|This bit provides the clock status of LPUART 2 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1518 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>11<br>BLOCK75|Function<br>IP block status<br>This bit provides the clock status of LPUART 1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|---|---|
|10<br>BLOCK74|IP block status<br>This bit provides the clock status of LPUART 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|9|IP block status|
|BLOCK73|This bit provides the clock status of FlexIO in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|8<br>BLOCK72|IP block status<br>This bit provides the clock status of block 72 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|7<br>BLOCK71|IP block status<br>This bit provides the clock status of block 71 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|6<br>BLOCK70|IP block status<br>This bit provides the clock status of FlexCAN 5 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|5<br>BLOCK69|IP block status<br>This bit provides the clock status of FlexCAN 4 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|4<br>BLOCK68|IP block status<br>This bit provides the clock status of FlexCAN 3 in partition 1.<br>0b - Clock is not running.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1519 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Clock is running.|
|3|IP block status|
|BLOCK67|This bit provides the clock status of FlexCAN 2 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|2<br>BLOCK66|IP block status<br>This bit provides the clock status of FlexCAN 1 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|1|IP block status|
|BLOCK65|This bit provides the clock status of FlexCAN 0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|0<br>—|Reserved<br>This field is reserved and read returns zeros.|



### 44.7.34 Partition 1 COFB Set 3 Clock Status Register (PRTN1_COFB3_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB3_STAT|31Ch|



#### Function 

This register provides the status of set 3 of COFBs inside partition 1. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1520 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1521-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0 0 0<br>K110  K108  K107  K106  K105  K104  K103  K102  K101  K99  K98  K97  K96<br>W<br>Reset 0 1 0 1 1 1 1 1 1 1 1 0 1 1 1 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>—|Reserved<br>This field is reserved and read returns zeros.|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1521 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15<br>—|Reserved<br>This field is reserved and read returns zeros.|
|14|IP block status|
|BLOCK110|This bit provides the clock status of block 110 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12|IP block status|
|BLOCK108|This bit provides the clock status of SELFTEST GPR in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|11|IP block status|
|BLOCK107|This bit provides the clock status of block 107 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|10|IP block status|
|BLOCK106|This bit provides the clock status of block 106 in partition 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1522 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is not running.<br>1b - Clock is running.|
|9<br>BLOCK105|IP block status<br>This bit provides the clock status of block 105 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|8<br>BLOCK104|IP block status<br>This bit provides the clock status of STCU in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|7|IP block status|
|BLOCK103|This bit provides the clock status of Configuartion_GPR in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|6|IP block status|
|BLOCK102|This bit provides the clock status of block 102 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|5|IP block status|
|BLOCK101|This bit provides the clock status of JDC in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>BLOCK99|IP block status<br>This bit provides the clock status of MU_0 in partition 1.<br>0b - Clock is not running.<br>1b - Clock is running.|
|2|IP block status|
|BLOCK98|This bit provides the clock status of MTR in partition 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1523 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is not running.<br>1b - Clock is running.|
|1|IP block status|
|BLOCK97|This bit provides the clock status of FCCU in partition 1.|
||0b - Clock is not running.|
||1b - Clock is running.|
|0|IP block status|
|BLOCK96|This bit provides the clock status of CRC in partition 1.<br>0b - Clock is not running.|
||1b - Clock is running.|



### 44.7.35 Partition 1 COFB Set 0 Clock Enable Register (PRTN1_COFB0_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB0_CLKEN|330h|



#### Function 

This register provides clock control signaling to the individual COFBs in set 0 inside partition 1. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1524-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R REQ3 0 REQ2 REQ2 0 0 0 REQ2 REQ2 0 REQ2 0 0 0 0 0<br>W 1  9  8  4  3  1<br>Reset 0 1 0 1 1 1 1 0 0 0 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R REQ1 REQ1 REQ1 REQ1 REQ1 REQ1 0 0 0<br>REQ9  REQ8  REQ7  REQ6  REQ5  REQ4  REQ3<br>W 5  4  3  2  1  0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1524 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Fields 

|Field|Function|
|---|---|
|31|Clock enable|
|REQ31|This bit provides the clock enable control for INTM in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>REQ29|Clock enable<br>This bit provides the clock enable control for STM 0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|28<br>REQ28|Clock enable<br>This bit provides the clock enable control for SWT 0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>—|Reserved<br>This field is reserved and read returns zeros.|
|24<br>REQ24|Clock enable<br>This bit provides the clock enable control for MSCM in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|23|Clock enable|
|REQ23|This bit provides the clock enable control for block 23 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|22|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1525 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>21<br>REQ21|Function<br>Clock enable<br>This bit provides the clock enable control for SDA-AP in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|---|---|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15|Clock enable|
|REQ15|This bit provides the clock enable control for eDMA TCD 11 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|14<br>REQ14|Clock enable<br>This bit provides the clock enable control for eDMA TCD 10 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|13<br>REQ13|Clock enable<br>This bit provides the clock enable control for eDMA TCD 9 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|12<br>REQ12|Clock enable<br>This bit provides the clock enable control for eDMA TCD 8 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1526 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>11|Function<br>Clock enable|
|---|---|
|REQ11|This bit provides the clock enable control for eDMA TCD7 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|10<br>REQ10|Clock enable<br>This bit provides the clock enable control for eDMA TCD 6 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|9<br>REQ9|Clock enable<br>This bit provides the clock enable control for eDMA TCD 5 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|8<br>REQ8|Clock enable<br>This bit provides the clock enable control for eDMA TCD 4 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|7<br>REQ7|Clock enable<br>This bit provides the clock enable control for eDMA TCD 3 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|6<br>REQ6|Clock enable<br>This bit provides the clock enable control for eDMA TCD 2 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|5<br>REQ5|Clock enable<br>This bit provides the clock enable control for eDMA TCD 1 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|4<br>REQ4|Clock enable<br>This bit provides the clock enable control for eDMA in partition 1.<br>0b - Clock is turned off.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1527 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Clock is turned on.|
|3|Clock enable|
|REQ3|This bit provides the clock enable control for eDMA in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0<br>—|Reserved<br>This field is reserved and read returns zeros.|



### 44.7.36 Partition 1 COFB Set 1 Clock Enable Register (PRTN1_COFB1_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB1_CLKEN|334h|



#### Function 

This register provides clock control signaling to the individual COFBs in set 1 inside partition 1. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1528 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1529-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R REQ6 0 0 0 0 0 REQ5 REQ5 0 0 REQ5 0 REQ5 0 REQ4 0<br>W 3  7  6  3  1  9<br>Reset 0 1 1 1 1 1 0 0 1 1 1 1 1 1 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R REQ4 0 REQ4 0 0 REQ4 0 0 0 0 0 0 0 REQ3 REQ3 REQ3<br>W 7  5  2  4  3  2<br>Reset 0 0 1 0 1 1 1 1 1 1 1 1 1 1 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Clock enable|
|REQ63|This bit provides the clock enable control for PIT 2 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25|Clock enable|
|REQ57|This bit provides the clock enable control for PLL 2 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|24|Clock enable|
|REQ56|This bit provides the clock enable control for PLL in partition 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1529 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is turned off.<br>1b - Clock is turned on.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>REQ53|Clock enable<br>This bit provides the clock enable control for FXOSC in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19|Clock enable|
|REQ51|This bit provides the clock enable control for SXOSC in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>REQ49|Clock enable<br>This bit provides the clock enable control for TSPC in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15|Clock enable|
|REQ47|This bit provides the clock enable control for CMU_0-5 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1530 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>13|Function<br>Clock enable|
|---|---|
|REQ45|This bit provides the clock enable control for WKPU in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10<br>REQ42|Clock enable<br>This bit provides the clock enable control for SIUL_VIRTWRAPPER_PDAC3 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|9<br>—|Reserved<br>This field is reserved and read returns zeros.|
|8<br>—|Reserved<br>This field is reserved and read returns zeros.|
|7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>—|Reserved<br>This field is reserved and read returns zeros.|
|2<br>REQ34|Clock enable<br>This bit provides the clock enable control for RTC in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1531 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Clock enable|
|REQ33|This bit provides the clock enable control for DMAMUX 1 in partition 1.|
||0b - Clock is turned off.|
||1b - Clock is turned on.|
|0|Clock enable|
|REQ32|This bit provides the clock enable control for DMAMUX 0 in partition 1.|
||0b - Clock is turned off.|
||1b - Clock is turned on.|



### 44.7.37 Partition 1 COFB Set 2 Clock Enable Register (PRTN1_COFB2_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB2_CLKEN|338h|



#### Function 

This register provides clock control signaling to the individual COFBs in set 2 inside partition 1. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1532-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R REQ9 0 REQ9 REQ9 REQ9 0 REQ8 REQ8 REQ8 REQ8 REQ8 REQ8 0 0 REQ8 REQ8<br>W 5  3  2  1  9  8  7  6  5  4  1  0<br>Reset 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R REQ7 REQ7 REQ7 REQ7 REQ7 REQ7 REQ7 REQ7 REQ7 REQ7 REQ6 REQ6 REQ6 REQ6 REQ6 0<br>W 9  8  7  6  5  4  3  2  1  0  9  8  7  6  5<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1532 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Fields 

|Field|Function|
|---|---|
|31|Clock enable|
|REQ95|This bit provides the clock enable control for TMU in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>REQ93|Clock enable<br>This bit provides the clock enable control for LPCMP 1 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|28<br>REQ92|Clock enable<br>This bit provides the clock enable control for LPCMP 0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|27<br>REQ91|Clock enable<br>This bit provides the clock enable control for SAI_0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25|Clock enable|
|REQ89|This bit provides the clock enable control for LPSPI 3 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|24|Clock enable|
|REQ88|This bit provides the clock enable control for LPSPI 2 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|23|Clock enable|
|REQ87|This bit provides the clock enable control for LPSPI 1 in partition 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1533 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is turned off.<br>1b - Clock is turned on.|
|22<br>REQ86|Clock enable<br>This bit provides the clock enable control for LPSPI 0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|21<br>REQ85|Clock enable<br>This bit provides the clock enable control for LPI2C 1 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|20|Clock enable|
|REQ84|This bit provides the clock enable control for LPI2C 0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17|Clock enable|
|REQ81|This bit provides the clock enable control for LPUART 7 in partition 1.|
||0b - Clock is turned off.<br>1b - Clock is turned on.|
|16|Clock enable|
|REQ80|This bit provides the clock enable control for LPUART 6 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|15|Clock enable|
|REQ79|This bit provides the clock enable control for LPUART 5 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|14|Clock enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1534 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|REQ78|This bit provides the clock enable control for LPUART 4 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|13<br>REQ77|Clock enable<br>This bit provides the clock enable control for LPUART 3 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|12|Clock enable|
|REQ76|This bit provides the clock enable control for LPUART 2 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|11<br>REQ75|Clock enable<br>This bit provides the clock enable control for LPUART 1 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|10|Clock enable|
|REQ74|This bit provides the clock enable control for LPUART 0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|9|Clock enable|
|REQ73|This bit provides the clock enable control for FlexIO in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|8|Clock enable|
|REQ72|This bit provides the clock enable control for block 72 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|7|Clock enable|
|REQ71|This bit provides the clock enable control for block 71 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1535 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|6|Clock enable|
|REQ70|This bit provides the clock enable control for FlexCAN 5 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|5|Clock enable|
|REQ69|This bit provides the clock enable control for FlexCAN 4 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|4|Clock enable|
|REQ68|This bit provides the clock enable control for FlexCAN 3 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|3<br>REQ67|Clock enable<br>This bit provides the clock enable control for FlexCAN 2 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|2|Clock enable|
|REQ66|This bit provides the clock enable control for FlexCAN 1 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|1<br>REQ65|Clock enable<br>This bit provides the clock enable control for FlexCAN 0 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|0<br>—|Reserved<br>This field is reserved and read returns zeros.|



### 44.7.38 Partition 1 COFB Set 3 Clock Enable Register (PRTN1_COFB3_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN1_COFB3_CLKEN|33Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1536 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Function 

This register provides clock control signaling to the individual COFBs in set 3 inside partition 1. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1537-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0 REQ1 0 REQ1 0 0 0 0 0 REQ9<br>W 04  02  6<br>Reset 0 1 0 1 1 1 1 1 1 1 1 0 1 1 1 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1537 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15<br>—|Reserved<br>This field is reserved and read returns zeros.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1538 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|9<br>—|Reserved<br>This field is reserved and read returns zeros.|
|8<br>REQ104|Clock enable<br>This bit provides the clock enable control for STCU in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6|Clock enable|
|REQ102|This bit provides the clock enable control for block 102 in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>—|Reserved<br>This field is reserved and read returns zeros.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0<br>REQ96|Clock enable<br>This bit provides the clock enable control for CRC in partition 1.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1539 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.39 Partition 2 Process Configuration Register (PRTN2_PCONF) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_PCONF|500h|



#### Function 

This register provides a configuration for the hardware processes corresponding to partition 2. Each of the configuration bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding field in the PRTN2_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN2_PCONF and PRTN2_PUPD registers are used to determine the hardware processes to be executed. These are triggered in parallel and independent of each other. All dependent processes should be requested one after another from the software. 

~~<mark>NOTE</mark>~~ 

The partition clock enable/disable and output safe stating enable/disable are not standalone and must be done coherently in a fixed sequence. For details, see Software Reset Partition Turn-On Flow Chart and Software reset partition turn-off flowchart in Reset chapter. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1540-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0<br>PCE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-7|Reserved|
|—|This field is reserved and read returns zeros.|
|6|Reserved|
|—|This field is reserved and read returns zeros.|
|5|Reserved|
|—|This field is reserved and read returns zeros.|
|4|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1540 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|3|Reserved|
|—|This field is reserved and read returns zeros.|
|2|Reserved|
|—|This field is reserved and read returns zeros.|
|1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Partition clock enable|
|PCE|This bit controls whether the clock to IPs (other than core(s)) in the partition should be enabled or disabled.|
||0b - Disable the clock to IPs<br>1b - Enable the clock to IPs|



### 44.7.40 Partition 2 Process Update Register (PRTN2_PUPD) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_PUPD|504h|



#### Function 

This register provides trigger signaling for the hardware processes corresponding to partition 2. Each of the control bit acts as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value in the corresponding bit field in the PRTN2_PCONF register. When the hardware process is finished the corresponding bit in this register is auto-cleared to logic-0. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1541-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0<br>PCUD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1541 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Fields 

|Field|Function|
|---|---|
|31-7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5|Reserved|
|—|This field is reserved and read returns zeros.|
|4|Reserved|
|—|This field is reserved and read returns zeros.|
|3<br>—|Reserved<br>This field is reserved and read returns zeros.|
|2|Reserved|
|—|This field is reserved and read returns zeros.|
|1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Partition clock update|
|PCUD|This bit controls whether the hardware processes for enabling/disabling the clock to IPs (other than core(s))<br>in the partition should be triggered or not.<br>0b - Do not trigger the hardware process|
||1b - Trigger the hardware process|



### 44.7.41 Partition 2 Status Register (PRTN2_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_STAT|508h|



#### Function 

This register provides the current status of the control signals from the partition 2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1542 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||0|0|0|0|0|0|PCS|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



#### Fields 

|Field|Function|
|---|---|
|31-7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5<br>—|Reserved<br>This field is reserved and read returns zeros.|
|4<br>—|Reserved<br>This field is reserved and read returns zeros.|
|3<br>—|Reserved<br>This field is reserved and read returns zeros.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0|Partition clock status|
|PCS|This bit provides the status of the clock to partition.<br>0b - Clock is inactive|
||1b - Clock is active|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1543 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

### 44.7.42 Partition 2 COFB Set 0 Clock Status Register (PRTN2_COFB0_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_COFB0_STAT|510h|



#### Function 

This register provides the status of set 0 of COFBs inside partition 2. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 2. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1544-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0<br>K30  K29  K28  K27  K26  K25  K24  K23  K22  K21  K20  K19  K18  K17  K16<br>W<br>Reset 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0<br>K15  K14  K13  K12  K11  K10  K9  K8  K7  K6  K5  K4  K2  K1  K0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30|IP block status|
|BLOCK30|This bit provides the clock status of STM 2 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|29|IP block status|
|BLOCK29|This bit provides the clock status of STM 1 in partition 2.<br>0b - Clock is not running.|
||1b - Clock is running.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1544 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>28|Function<br>IP block status|
|---|---|
|BLOCK28|This bit provides the clock status of SWT 2 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|27<br>BLOCK27|IP block status<br>This bit provides the clock status of SWT 1 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|26<br>BLOCK26|IP block status<br>This bit provides the clock status of PRAM 2 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|25<br>BLOCK25|IP block status<br>This bit provides the clock status of PRAM 1 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|24<br>BLOCK24|IP block status<br>This bit provides the clock status of SEMA42 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|23<br>BLOCK23|IP block status<br>This bit provides the clock status of eDMA TCD 31 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|22<br>BLOCK22|IP block status<br>This bit provides the clock status of eDMA TCD 30 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|21<br>BLOCK21|IP block status<br>This bit provides the clock status of eDMA TCD 29 in partition 2.<br>0b - Clock is not running.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1545 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Clock is running.|
|20|IP block status|
|BLOCK20|This bit provides the clock status of eDMA TCD 28 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|19<br>BLOCK19|IP block status<br>This bit provides the clock status of eDMA TCD27 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|18<br>BLOCK18|IP block status<br>This bit provides the clock status of eDMA TCD 26 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|17|IP block status|
|BLOCK17|This bit provides the clock status of eDMA TCD 25 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|16|IP block status|
|BLOCK16|This bit provides the clock status of eDMA TCD 24 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|15<br>BLOCK15|IP block status<br>This bit provides the clock status of eDMA TCD 23 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|14|IP block status|
|BLOCK14|This bit provides the clock status of eDMA TCD 22 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|13|IP block status|
|BLOCK13|This bit provides the clock status of eDMA TCD 21 in partition 2.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1546 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is not running.<br>1b - Clock is running.|
|12<br>BLOCK12|IP block status<br>This bit provides the clock status of eDMA TCD 20 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|11|IP block status|
|BLOCK11|This bit provides the clock status of eDMA TCD 19 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|10|IP block status|
|BLOCK10|This bit provides the clock status of eDMA TCD 18 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|9<br>BLOCK9|IP block status<br>This bit provides the clock status of eDMA TCD 17 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|8|IP block status|
|BLOCK8|This bit provides the clock status of eDMA TCD 16 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|7|IP block status|
|BLOCK7|This bit provides the clock status of eDMA TCD 15 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|6|IP block status|
|BLOCK6|This bit provides the clock status of eDMA TCD 14 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|5|IP block status<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1547 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|BLOCK5|This bit provides the clock status of eDMA TCD 13 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|4<br>BLOCK4|IP block status<br>This bit provides the clock status of eDMA TCD 12 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|3<br>—|Reserved<br>This field is reserved and read returns zeros.|
|2<br>BLOCK2|IP block status<br>This bit provides the clock status of PRAM2_TCM_XBIC in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|1<br>BLOCK1|IP block status<br>This bit provides the clock status of eDMA_XBIC in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|0<br>BLOCK0|IP block status<br>This bit provides the clock status of TCM_XBIC in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|



### 44.7.43 Partition 2 COFB Set 1 Clock Status Register (PRTN2_COFB1_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_COFB1_STAT|514h|



#### Function 

This register provides the status of set 1 of COFBs inside partition 2. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1548 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1549-01.png)


<!-- Start of picture text -->
Mode Entry Module (MC_ME)<br><!-- End of picture text -->

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1549-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0 0 0 0 0 0 0 0<br>K63  K62  K59  K58  K57  K55  K51  K48<br>W<br>Reset 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC BLOC<br>R 0 0 0 0 0 0<br>K47  K42  K41  K40  K39  K38  K37  K36  K35  K33<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>BLOCK63|IP block status<br>This bit provides the clock status of block 63 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|30<br>BLOCK62|IP block status<br>This bit provides the clock status of block 62 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>BLOCK59|IP block status<br>This bit provides the clock status of MU_1 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|26<br>BLOCK58|IP block status<br>This bit provides the clock status of LPCMP2 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|25|IP block status<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1549 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|BLOCK57|This bit provides the clock status of uSDHC in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>BLOCK55|IP block status<br>This bit provides the clock status of SAI1 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>BLOCK51|IP block status<br>This bit provides the clock status of QuadSPI in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>BLOCK48|IP block status<br>This bit provides the clock status of LPSPI 5 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|15<br>BLOCK47|IP block status<br>This bit provides the clock status of LPSPI 4 in partition 2.<br>0b - Clock is not running.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1550 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function<br>1b - Clock is running.|
|---|---|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10|IP block status|
|BLOCK42|This bit provides the clock status of LPUART 15 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|9|IP block status|
|BLOCK41|This bit provides the clock status of LPUART 14 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|8|IP block status|
|BLOCK40|This bit provides the clock status of LPUART 13 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|7|IP block status|
|BLOCK39|This bit provides the clock status of LPUART 12 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|6|IP block status|
|BLOCK38|This bit provides the clock status of LPUART 11 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|5|IP block status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1551 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|BLOCK37|This bit provides the clock status of LPUART 10 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|4<br>BLOCK36|IP block status<br>This bit provides the clock status of LPUART 9 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|3<br>BLOCK35|IP block status<br>This bit provides the clock status of LPUART 8 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>BLOCK33|IP block status<br>This bit provides the clock status of GMAC in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|0<br>—|Reserved<br>This field is reserved and read returns zeros.|



### 44.7.44 Partition 2 COFB Set 2 Clock Status Register (PRTN2_COFB2_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_COFB2_STAT|518h|



#### Function 

This register provides the status of set 2 of COFBs inside partition 2. 

~~<mark>NOTE</mark>~~ 

The reset value of this register can vary depending on the availability of active clock pulses inside partition 2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1552 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1553-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BLOC BLOC BLOC BLOC<br>R 0 0 0 0 0 0 0 0 0 0 0 0<br>K69  K68  K67  K64<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|This field is reserved and read returns zeros.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>—|Reserved<br>This field is reserved and read returns zeros.|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1553 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15<br>—|Reserved<br>This field is reserved and read returns zeros.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10<br>—|Reserved<br>This field is reserved and read returns zeros.|
|9<br>—|Reserved<br>This field is reserved and read returns zeros.|
|8<br>—|Reserved<br>This field is reserved and read returns zeros.|
|7|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1554 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5<br>BLOCK69|IP block status<br>This bit provides the clock status of EIM2 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|4<br>BLOCK68|IP block status<br>This bit provides the clock status of EIM1 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|3|IP block status|
|BLOCK67|This bit provides the clock status of EIM0 in partition 2.<br>0b - Clock is not running.<br>1b - Clock is running.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0|IP block status|
|BLOCK64|This bit provides the clock status of block 64 in partition 2.<br>0b - Clock is not running.|
||1b - Clock is running.|



### 44.7.45 Partition 2 COFB Set 0 Clock Enable Register (PRTN2_COFB0_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_COFB0_CLKEN|530h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1555 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Function 

This register provides clock control signaling to the individual COFBs in set 0 inside partition 2. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1556-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 REQ3 REQ2 REQ2 REQ2 0 0 REQ2 REQ2 REQ2 REQ2 REQ2 REQ1 REQ1 REQ1 REQ1<br>W 0  9  8  7  4  3  2  1  0  9  8  7  6<br>Reset 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R REQ1 REQ1 REQ1 REQ1 REQ1 REQ1 0 0 0 0<br>REQ9  REQ8  REQ7  REQ6  REQ5  REQ4<br>W 5  4  3  2  1  0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved<br>This field is reserved and read returns zeros.|
|30|Clock enable|
|REQ30|This bit provides the clock enable control for STM 2 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|29|Clock enable|
|REQ29|This bit provides the clock enable control for STM 1 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|28|Clock enable|
|REQ28|This bit provides the clock enable control for SWT 2 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|27|Clock enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1556 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|REQ27|This bit provides the clock enable control for SWT 1 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>—|Reserved<br>This field is reserved and read returns zeros.|
|24<br>REQ24|Clock enable<br>This bit provides the clock enable control for SEMA42 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|23<br>REQ23|Clock enable<br>This bit provides the clock enable control for eDMA TCD 31 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|22<br>REQ22|Clock enable<br>This bit provides the clock enable control for eDMA TCD 30 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|21<br>REQ21|Clock enable<br>This bit provides the clock enable control for eDMA TCD 29 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|20<br>REQ20|Clock enable<br>This bit provides the clock enable control for eDMA TCD 28 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|19<br>REQ19|Clock enable<br>This bit provides the clock enable control for eDMA TCD27 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1557 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field<br>18|Function<br>Clock enable|
|---|---|
|REQ18|This bit provides the clock enable control for eDMA TCD 26 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|17<br>REQ17|Clock enable<br>This bit provides the clock enable control for eDMA TCD 25 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|16|Clock enable|
|REQ16|This bit provides the clock enable control for eDMA TCD 24 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|15|Clock enable|
|REQ15|This bit provides the clock enable control for eDMA TCD 23 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|14|Clock enable|
|REQ14|This bit provides the clock enable control for eDMA TCD 22 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|13<br>REQ13|Clock enable<br>This bit provides the clock enable control for eDMA TCD 21 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|12<br>REQ12|Clock enable<br>This bit provides the clock enable control for eDMA TCD 20 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|11<br>REQ11|Clock enable<br>This bit provides the clock enable control for eDMA TCD 19 in partition 2.<br>0b - Clock is turned off.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1558 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function<br>1b - Clock is turned on.|
|---|---|
|10|Clock enable|
|REQ10|This bit provides the clock enable control for eDMA TCD 18 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|9<br>REQ9|Clock enable<br>This bit provides the clock enable control for eDMA TCD 17 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|8<br>REQ8|Clock enable<br>This bit provides the clock enable control for eDMA TCD 16 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|7<br>REQ7|Clock enable<br>This bit provides the clock enable control for eDMA TCD 15 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|6<br>REQ6|Clock enable<br>This bit provides the clock enable control for eDMA TCD 14 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|5<br>REQ5|Clock enable<br>This bit provides the clock enable control for eDMA TCD 13 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|4<br>REQ4|Clock enable<br>This bit provides the clock enable control for eDMA TCD 12 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|3|Reserved|
|—|This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1559 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|2|Reserved|
|—|This field is reserved and read returns zeros.|
|1|Reserved|
|—|This field is reserved and read returns zeros.|
|0|Reserved|
|—|This field is reserved and read returns zeros.|



### 44.7.46 Partition 2 COFB Set 1 Clock Enable Register (PRTN2_COFB1_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_COFB1_CLKEN|534h|



#### Function 

This register provides clock control signaling to the individual COFBs in set 1 inside partition 2. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1560-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R REQ6 REQ6 0 0 0 REQ5 REQ5 0 REQ5 0 0 0 REQ5 0 0 REQ4<br>W 3  2  8  7  5  1  8<br>Reset 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R REQ4 0 0 0 0 REQ4 REQ4 REQ4 REQ3 REQ3 REQ3 REQ3 REQ3 0 REQ3 0<br>W 7  2  1  0  9  8  7  6  5  3<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1560 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Fields 

|Field|Function|
|---|---|
|31|Clock enable|
|REQ63|This bit provides the clock enable control for block 63 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|30<br>REQ62|Clock enable<br>This bit provides the clock enable control for block 62 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>REQ58|Clock enable<br>This bit provides the clock enable control for LPCMP2 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|25<br>REQ57|Clock enable<br>This bit provides the clock enable control for uSDHC in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>REQ55|Clock enable<br>This bit provides the clock enable control for SAI1 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1561 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>REQ51|Clock enable<br>This bit provides the clock enable control for QuadSPI in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|18<br>—|Reserved<br>This field is reserved and read returns zeros.|
|17<br>—|Reserved<br>This field is reserved and read returns zeros.|
|16<br>REQ48|Clock enable<br>This bit provides the clock enable control for LPSPI 5 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|15<br>REQ47|Clock enable<br>This bit provides the clock enable control for LPSPI 4 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10|Clock enable|
|REQ42|This bit provides the clock enable control for LPUART 15 in partition 2.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1562 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is turned off.<br>1b - Clock is turned on.|
|9|Clock enable|
|REQ41|This bit provides the clock enable control for LPUART 14 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|8|Clock enable|
|REQ40|This bit provides the clock enable control for LPUART 13 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|7|Clock enable|
|REQ39|This bit provides the clock enable control for LPUART 12 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|6|Clock enable|
|REQ38|This bit provides the clock enable control for LPUART 11 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|5|Clock enable|
|REQ37|This bit provides the clock enable control for LPUART 10 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|4|Clock enable|
|REQ36|This bit provides the clock enable control for LPUART 9 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|3|Clock enable|
|REQ35|This bit provides the clock enable control for LPUART 8 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|2|Reserved|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1563 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|1|Clock enable|
|REQ33|This bit provides the clock enable control for GMAC in partition 2.|
||0b - Clock is turned off.|
||1b - Clock is turned on.|
|0|Reserved|
|—|This field is reserved and read returns zeros.|



### 44.7.47 Partition 2 COFB Set 2 Clock Enable Register (PRTN2_COFB2_CLKEN) 

#### Offset 

|Register|Offset|
|---|---|
|PRTN2_COFB2_CLKEN|538h|



#### Function 

This register provides clock control signaling to the individual COFBs in set 2 inside partition 2. Whenever a partition clock enable (non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock to the corresponding block in the partition. 

~~<mark>NOTE</mark>~~ 

The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific MC_ME information for clock source availability. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/044_Mode_Entry_Module_-MC_ME-/S32K3XXRM_数据表.pdf-1564-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0 0 0 0 REQ6 REQ6 REQ6 0 0 REQ6<br>W 9  8  7  4<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1564 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

#### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved<br>This field is reserved and read returns zeros.|
|30<br>—|Reserved<br>This field is reserved and read returns zeros.|
|29<br>—|Reserved<br>This field is reserved and read returns zeros.|
|28<br>—|Reserved<br>This field is reserved and read returns zeros.|
|27<br>—|Reserved<br>This field is reserved and read returns zeros.|
|26<br>—|Reserved<br>This field is reserved and read returns zeros.|
|25<br>—|Reserved<br>This field is reserved and read returns zeros.|
|24<br>—|Reserved<br>This field is reserved and read returns zeros.|
|23<br>—|Reserved<br>This field is reserved and read returns zeros.|
|22<br>—|Reserved<br>This field is reserved and read returns zeros.|
|21<br>—|Reserved<br>This field is reserved and read returns zeros.|
|20<br>—|Reserved<br>This field is reserved and read returns zeros.|
|19<br>—|Reserved<br>This field is reserved and read returns zeros.|
|18<br>—<br>17|Reserved<br>This field is reserved and read returns zeros.<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1565 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—|This field is reserved and read returns zeros.|
|16<br>—|Reserved<br>This field is reserved and read returns zeros.|
|15<br>—|Reserved<br>This field is reserved and read returns zeros.|
|14<br>—|Reserved<br>This field is reserved and read returns zeros.|
|13<br>—|Reserved<br>This field is reserved and read returns zeros.|
|12<br>—|Reserved<br>This field is reserved and read returns zeros.|
|11<br>—|Reserved<br>This field is reserved and read returns zeros.|
|10<br>—|Reserved<br>This field is reserved and read returns zeros.|
|9<br>—|Reserved<br>This field is reserved and read returns zeros.|
|8<br>—|Reserved<br>This field is reserved and read returns zeros.|
|7<br>—|Reserved<br>This field is reserved and read returns zeros.|
|6<br>—|Reserved<br>This field is reserved and read returns zeros.|
|5|Clock enable|
|REQ69|This bit provides the clock enable control for EIM2 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|4|Clock enable|
|REQ68|This bit provides the clock enable control for EIM1 in partition 2.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1566 / 4640 

NXP Semiconductors 

Mode Entry Module (MC_ME) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is turned off.<br>1b - Clock is turned on.|
|3|Clock enable|
|REQ67|This bit provides the clock enable control for EIM0 in partition 2.<br>0b - Clock is turned off.<br>1b - Clock is turned on.|
|2<br>—|Reserved<br>This field is reserved and read returns zeros.|
|1<br>—|Reserved<br>This field is reserved and read returns zeros.|
|0|Clock enable|
|REQ64|This bit provides the clock enable control for block 64 in partition 2.<br>0b - Clock is turned off.|
||1b - Clock is turned on.|



## 44.8 Glossary 

WFI Wait for interrupt 

COFB Collection of functional blocks also referred as number of peripherals 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1567 / 4640 

