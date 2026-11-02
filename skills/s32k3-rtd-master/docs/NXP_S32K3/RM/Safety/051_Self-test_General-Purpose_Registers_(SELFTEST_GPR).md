NXP Semiconductors 

# Chapter 51 Self-test General-Purpose Registers (SELFTEST_GPR) 

## 51.1 Introduction 

SELFTEST_GPR configures the STCU2 LBIST shift cycles. Programming self-test GPRs is a part of the self-test programming sequence. See the "Self-test programming sequence" section in the STCU2 chapter. 

NXP supports only STCU2 Built-In Self-Test (BIST) sequences that have been validated by NXP for in-field testing usage. 

The detailed programming sequences for supported configurations are available in a separate application note (contact your NXP sales representative). 

The values for SELFTEST_GPR registers must be aligned with the NXP supported configurations only. 

~~<mark>NOTE</mark>~~ 

SELFTEST_GPR is not present in S32K312 and S32K311. 

~~<mark>NOTE</mark>~~ 

While accessing SELFTEST_GPR space, software must ensure that the STCU2 block has its clock enabled, i.e., MC_ME.PRTN1_COFB3_CLKEN[REQ104] configured as 1'b1. Not ensuring this might result in unpredictable device behaviour. 

## 51.2 Peripheral shift clock switching (PCS) 

The PCS feature is used to avoid current surges at the start and/or end of LBIST. Since LBIST can cause sudden current surges which might lead to chip malfunction. 

With PCS enabled, there are additional (SELFTEST_GPR.CONFIG_GPR[PCS_STEP_SIZE] + 1)*16 patterns beyond the configured count. If enabled at the start of LBIST (using SELFTEST_GPR.CONFIG_GPR[PCS_ENABLE_START]), it would cause the shift clock to scale up in this duration from divide by 16 to the original frequency (by changing divider in each step). 

Similarly, if configured at the end of LBIST (using SELFTEST_GPR.CONFIG_GPR[PCS_ENABLE_END]), the shift clock frequency will be scaled down from original frequency to divide by 16. 

## 51.3 SELFTEST_GPR register descriptions 

### 51.3.1 SELFTEST_GPR memory map 

SELFTEST_GPR base address: 403B_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Configuration register (CONFIG_REG)|32|RW|0000_ADD5h|
|14h|LBIST Program (LBIST_PROG_REG)|32|RW|0003_0050h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1778 / 4640 

NXP Semiconductors 

Self-test General-Purpose Registers (SELFTEST_GPR) 

### 51.3.2 Configuration register (CONFIG_REG) 

#### Offset 

|Register|Offset|
|---|---|
|CONFIG_REG|0h|



#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserv<br>ed|||||||Rese|rved|||||||Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Reserved||||PCS_E<br>NA...|PCS_E<br>NA...|PCS|_STEP_|SIZE||Rese|rved||
|Reset|1|0|1|0|1|1|0|1|1|1|0|1|0|1|0|1|



#### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-17<br>—|Reserved|
|16<br>—|Reserved|
|15-9<br>—|Reserved|
|8|PCS Enable End|
|PCS_ENABLE_<br>END|Enables Progressive Shift Clock Switching for LBIST at end. The feature gets enabled when this bit is<br>set to 1. It is recommended to run LBIST patterns by enabling this feature.|
|7|PCS Enable Start|
|PCS_ENABLE_<br>START|Enables Progressive Shift Clock Switching for LBIST at start. The feature gets enabled when this bit is<br>set to 1. It is recommended to run LBIST patterns by enabling this feature.|
|6-4|PCS Step Size|
||pcs_step_size[2:0] controls the step size for progressive increase of shift frequency:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1779 / 4640 

NXP Semiconductors 

Self-test General-Purpose Registers (SELFTEST_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|PCS_STEP_SIZ<br>E|000 - step size of 1 pattern<br>001 - step size of 2 patterns|
||...|
||111 - step size of 8 patterns|
|3-0<br>—|Reserved|



### 51.3.3 LBIST Program (LBIST_PROG_REG) 

#### Offset 

|Register|Offset|
|---|---|
|LBIST_PROG_REG|14h|



#### Function 

Configures the LBIST shift count. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Rese|rved||||||LB|IST_SHIF|T_COUNT||||
|Reset|0|0|0|0|0|0|0|0|0|1|0|1|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|LBIST Shift Count|
|LBIST_SHIFT_<br>COUNT|Specifies the number of shift cycles in ascan chainin onepattern countfor the LBIST partition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1780 / 4640 

NXP Semiconductors 

Self-test General-Purpose Registers (SELFTEST_GPR) 

## 51.4 Glossary 

- BIST clock The BIST clock refers to the BIST operational clock which is the clock source used while LBIST is operational by the LBIST controller, which is the MC_CGM clock node LBIST_CLK for the chip. See the system block diagram for details. 

- LBIST Logic built-in self-test 

- Pattern The pattern count refers to an empirically determined value of shift patterns run in LBIST on a scan chain count to result in predetermined fault coverage, based on device safety integrity level. Since the LBIST scheme is Pseudo Random Testing, a sufficiently good value of pattern count is used which provides the required fault coverage. 

- Scan chain A sequential chain of flops in scan mode over which one scan pattern (generated by PRPG, that is, Pseudo Random Pattern Generator) in LBIST will be shifted and the output MISR (Multi Input Signature Register) will be matched with earlier known value to determine pass or fail criterion of that particular chain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1781 / 4640 

