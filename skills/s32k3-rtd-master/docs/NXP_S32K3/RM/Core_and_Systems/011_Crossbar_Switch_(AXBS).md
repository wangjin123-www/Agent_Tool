NXP Semiconductors 

# Chapter 11 Crossbar Switch (AXBS) 

## 11.1 Chip-specific AXBS information 

### 11.1.1 AXBS instances and connectivity matrix 

This chip has up to 5 instances of AXBS. 

Table 37. AXBS instances 

|Instance|K358|K3x4|K342|K312|K311|
|---|---|---|---|---|---|
|AXBS_0|Yes|Yes|Yes|Yes|Yes|
|AXBS_1|Yes|Yes|Yes|No|No|
|AXBS_2|Yes|Yes|Yes|No|No|
|AXBS_3|Yes|Yes|Yes|No|No|
|AXBS_4|Yes|Yes|Yes|No|No|



Table 38. AXBS connectivity matrix for K358 

|Instance<br>|Master an|d slave assignments|||
|---|---|---|---|---|
|AXBS_0 (main)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|Cortex-M7_0 AHBM|S0|Flash memory port 0|
||M1|AXBS_2 S0|S1|Flash memory port 1|
||M2|AXBS_4 S0|S2|PRAM_0|
||M3|GMAC|S3|PRAM2_TCM splitter|
||M4|Cortex-M7_1 AHBM|S4|Flash memory port 2|
||M5|Cortex-M7_2 AHBM|S5|QuadSPI|
||M6|uSDHC|S6|PRAM_1|
||||S7|Flash memory port 3|
|AXBS_1 (peripheral)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|Cortex-M7_0 AHBP|S0|AIPS_0|
||M1|AXBS_2 S1|S1|AIPS_1|
||M2|AXBS_4 S1|S2|AIPS_2|
||M3|Cortex-M7_1 AHBP|||
||M4|Cortex-M7_2 AHBP|||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

377 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

Table 38. AXBS connectivity matrix for K358 (continued) 

|Instance|Master an|d slave assignments|||
|---|---|---|---|---|
|AXBS_2 (eDMA)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|eDMA|S0|AXBS_0 M1|
||M1|Reserved|S1|AXBS_1 M1|
|AXBS_3 (Cortex-M7 TCM)|Not applic|able|||
|AXBS_4 (HSE)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|HSE_B|S0|AXBS_0 M2|
||||S1|AXBS_1 M2|
|AXBS_5 (TCM_PRAM)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|AXBS_0 S3|S0|PRAM_2|
||||S1|Cortex-M7_0 TCM|
||||S2|Cortex-M7_1 TCM|
||||S3|Cortex-M7_2 TCM|



Table 39. AXBS connectivity matrix for K344, K324, K314, and K342 

|Instance<br>|Master an|d slave assignments|||
|---|---|---|---|---|
|AXBS_0 (main)|||||
|<br>|Master<br>port|Master module|Slave port|Slave module|
||M0|Cortex-M7_0 AHBM|S0|Flash memory port 0|
||M1|AXBS_2 S0|S1|Flash memory port 1|
||M2|HSE_B|S2|PRAM_0|
||M3|EMAC|S3|Cortex-M7 TCM|
||M4<sup>1</sup>|Cortex-M7_1 AHBM|S4|Flash memory port 2|
||||S5|QuadSPI|
||||S6|PRAM_1<sup>2</sup>|
||1. Thes<br>2. Thes|e ports are reserved for S32K314.<br>e ports are reserved for S32K342.|||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

378 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

Table 39. AXBS connectivity matrix for K344, K324, K314, and K342 (continued) 

|Instance|Master an|d slave assignments|||
|---|---|---|---|---|
|AXBS_1 (peripheral)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|Cortex-M7_0 AHBP|S0|AIPS_0|
||M1|AXBS_2 S1|S1|AIPS_1|
||M2|HSE_B|S2|AIPS_2|
||M3<sup>1</sup>|Cortex-M7_1 AHBP|||
|AXBS_2 (eDMA)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|eDMA|S0|AXBS_0 M1|
||||S1|AXBS_1 M1|
|AXBS_3 (Cortex-M7 TCM)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|AXBS_0 S3|S0|Cortex-M7_0 TCM|
||||S1<sup>1</sup>|Cortex-M7_1 TCM|
|AXBS_4 (HSE)|||||
||Master<br>port|Master module|Slave port|Slave module|
||M0|HSE_B|S0|AXBS_0 M2|
||||S1<sup>1</sup>|AXBS_1 M2|



Table 40. AXBS connectivity matrix for K311 and K312 

|Instance<br>|Master an|d slave assignments|||
|---|---|---|---|---|
|AXBS_0 (main)|||||
|<br>|Master<br>port|Master module|Slave port|Slave module|
||M0|Cortex-M7_0 AHBM|S0|Flash memory port 0|
||M1|AXBS_2 S0|S1|Flash memory port 1|
||M2|HSE_B|S2|PRAM_0|
||M3|EMAC|S3|Cortex-M7 TCM|
||M4|Reserved|S4|AIPS_0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

379 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

|Instance|Master and slave assignments|S5|AIPS_1|
|---|---|---|---|



## 11.2 Overview 

This section provides information on the layout, configuration, and programming of the crossbar switch. 

The crossbar switch connects bus masters and bus slaves using a crossbar switch structure. This structure allows all bus masters to access different bus slaves simultaneously, while providing arbitration among the bus masters when they access the same slave. A variety of bus arbitration methods and attributes may be programmed on a slave-by-slave basis. 

### 11.2.1 Features 

- Symmetric crossbar bus switch implementation 

   - Allows concurrent accesses from different masters to different slaves 

   - Slave arbitration attributes configured on a slave-by-slave basis 

- Single-clock 64-bit transfer 

- Support for burst transfers of 64 bits of data 

- Support for low-power park mode 

- Master high-priority elevation 

- 64-bit AHB crossbar bus switch compatible with ARM's AMBA Specification v2.0 

## 11.3 Functional description 

Information about general operation and arbitration is provided in this section. 

### 11.3.1 General operation 

When a master accesses the crossbar switch, the access is immediately taken. If the targeted slave port of the access is available, then the access is immediately presented on the slave port. Single-clock or zero-wait-state accesses are possible through the crossbar. If the targeted slave port of the access is busy or parked on a different master port, the requesting master sees wait states inserted until the targeted slave port can service the master's request. The latency in servicing the request depends on each master's priority level and the responding slave's access time. 

Because the crossbar switch appears to be just another slave to the master device, the master device has no knowledge of whether it actually owns the slave port it is targeting. The master waits while it does not have control of the slave port it is targeting. 

After the master acquires control of the slave port, it controls the port until it relinquishes the port by running an IDLE cycle or by targeting a different slave port for its next access. 

The master can also lose control of the slave port if another higher-priority master makes a request to the slave port. However, if the master is running a fixed-length burst transfer, it retains control of the slave port until that transfer completes. 

The crossbar terminates all master IDLE transfers, as opposed to allowing the termination to come from one of the slave buses. Additionally, when no master is requesting access to a slave port, the crossbar drives IDLE transfers onto the slave bus, even though a default master may be granted access to the slave port. 

When a slave bus is being idled by the crossbar, it can park the slave port on the master port indicated by CRSn[PARK]. This is done to save the initial clock of arbitration delay that otherwise would be seen if the same master had to arbitrate to gain control of the slave port. The slave port can also be put into low-power park mode to save power, by using CRSn[PCTL]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

380 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

### 11.3.2 Register coherency 

The operation of the crossbar is affected as soon as a register is written. The values of the registers do not track with slave-port-related master accesses, but instead track only with slave accesses. 

### 11.3.3 Arbitration 

The crossbar switch supports following arbitration algorithms: 

- Fixed priority 

- Round-robin 

The arbitration scheme is independently programmable for each slave port. 

#### 11.3.3.1 Fixed-priority operation 

When operating in fixed-priority mode, each master is assigned a unique priority level in the priority registers (PRSn). If two masters request access to the same slave port, the master with the highest priority in the selected priority register gains control over the slave port. 

~~<mark>NOTE</mark>~~ In this arbitration mode, a higher-priority master can monopolize a slave port, preventing accesses from any lower-priority master to the port. 

When a master makes a request to a slave port, the slave port checks whether the new requesting master's priority level is higher than that of the master that currently has control over the slave port, unless the slave port is in a parked state. The slave port performs an arbitration check at every clock edge to ensure that the master, if any, has control of the slave port. 

The following table describes possible scenarios based on the requesting master port. 

Table 41. Methods of how the crossbar switch grants control of a slave port to a master 

|When|Then the crossbar switch grants control to the requesting<br>master|
|---|---|
|Both of the following are true:<br>• The current master is not running a transfer.<br>• The new requesting master's priority level is higher than<br>that of the current master.|At the next clock edge|
|Both of the following are true:<br>• The current master is running a fixed length burst<br>transfer or a locked transfer.<br>• The requesting master's priority level is higher than that<br>of the current master.|At the end of the burst transfer or locked transfer|
|The requesting master's priority level is lower than the<br>current master.|At the conclusion of one of the following cycles:<br>• An IDLE cycle<br>• A non-IDLE cycle to a location other than the current<br>slave port|



#### 11.3.3.2 Round-robin priority operation 

When operating in round-robin mode, each master is assigned a relative priority based on the master port number. This relative priority is compared to the master port number (ID) of the last master to perform a transfer on the slave bus. The highest priority 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

381 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

requesting master owns the slave bus at the next transfer boundary, accounting for locked and fixed-length burst transfers. Priority is based on how far ahead the ID of the requesting master is to the ID of the last master. 

After a master is granted access to a slave port, a master may perform as many transfers as desired to that port until another master makes a request to the same slave port. The next master in line is granted access to the slave port at the next transfer boundary, or possibly on the next clock cycle, if the current master has no pending access request. 

As an example of arbitration in round-robin mode, assume that the crossbar is implemented with master ports 0, 1, 4, and 5. If the last master of the slave port was master 1, and masters 0, 4, and 5 make simultaneous requests, they are serviced in this order: 4,5, and then 0. 

Parking may continue to be used in a round-robin mode, but does not affect the round-robin pointer unless the parked master performs a transfer. Handoff occurs to the next master in line after one cycle of arbitration. If the slave port is put into low-power park mode, the round-robin pointer is reset to point at master port 0, giving it the highest priority. 

#### 11.3.3.3 Priority assignment 

Each master port must be assigned a unique 3-bit priority level. If an attempt is made to program multiple master ports with the same priority level within the priority registers (PRSn), the crossbar switch responds with a bus error and the registers are not updated. 

## 11.4 Initialization/application information 

No initialization is required for the crossbar switch. 

Hardware reset ensures that all the register bits used by the crossbar switch are properly initialized to a valid state. However, the following settings and priorities may be programmed to achieve the maximum system performance: 

- During the configuration of the crossbar switch, all other masters must be idle. 

- To prevent reconfiguration of the crossbar switch, write 1 to CRSn[RO]. 

## 11.5 Memory map and register definition 

Each slave port of the crossbar switch contains configuration registers. Read- and write-transfers require two bus clock cycles. The registers can be read from and written to only in supervisor mode. Additionally, these registers can be read from or written to only by 32-bit accesses. 

A bus error response is returned if an unimplemented location is accessed within the crossbar switch. 

The CRSn and PRSn registers can be programmed as read-only to prevent changes to their configuration. After being read-only protected, future writes to them terminate with a data storage error. 

~~<mark>NOTE</mark>~~ 

This section shows the registers for all eight master and slave ports. If a master or slave is not used on this particular chip, then unexpected results occur when writing to its registers. See the chip configuration details for the exact master and slave assignments for your chip. 

All references to the crossbar switch registers are based on the physical port connections. 

### 11.5.1 AXBS register descriptions 

#### 11.5.1.1 AXBS memory map 

AXBS_LITE base address: 4020_0000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

382 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Priority Slave Registers (PRS0)|32|RW|0654_3210h|
|10h|Control Register (CRS0)|32|RW|0002_0110h|
|100h|Priority Slave Registers (PRS1)|32|RW|0654_3210h|
|110h|Control Register (CRS1)|32|RW|0002_0110h|
|200h|Priority Slave Registers (PRS2)|32|RW|0654_3210h|
|210h|Control Register (CRS2)|32|RW|0002_0110h|
|300h|Priority Slave Registers (PRS3)|32|RW|0654_3210h|
|310h|Control Register (CRS3)|32|RW|0002_0110h|
|400h|Priority Slave Registers (PRS4)|32|RW|0654_3210h|
|410h|Control Register (CRS4)|32|RW|0002_0110h|
|500h|Priority Slave Registers (PRS5)|32|RW|0654_3210h|
|510h|Control Register (CRS5)|32|RW|0002_0110h|
|600h|Priority Slave Registers (PRS6)|32|RW|0654_3210h|
|610h|Control Register (CRS6)|32|RW|0002_0110h|
|700h|Priority Slave Registers (PRS7)|32|RW|0654_3210h|
|710h|Control Register (CRS7)|32|RW|0002_0110h|



#### 11.5.1.2 Priority Slave Registers (PRS0 - PRS7) 

##### Offset 

|Register|Offset|
|---|---|
|PRS0|0h|
|PRS1|100h|
|PRS2|200h|
|PRS3|300h|
|PRS4|400h|
|PRS5|500h|
|PRS6|600h|
|PRS7|700h|



##### Function 

The priority slave registers(PRSn) set the priority of each master port on a per slave port basis and reside in each slave port. The priority register can be accessed only with 32-bit accesses. After the CRSn[RO] bit is set, the PRSn register can only be read; attempts to write to it have no effect on PRSn and result in a bus-error response to the master initiating the write. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

383 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

Two available masters must not be programmed with the same priority level. Attempts to program two or more masters with the same priority level result in a bus-error response and the PRSn is not updated. 

~~<mark>NOTE</mark>~~ 

Valid values for the Mn priority fields depend on which masters are available on the chip. This information can be found in the chip-specific information for the crossbar. 

- If the chip contains fewer than three masters, only one bit is valid. 

- If the chip contains fewer than five masters, only two bits are valid. 

- If five or more masters are present, all three bits of the priority field are used. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||Reserved||0||M6||0||M5||0||M4||
|W|||-||||||||||||||
|Reset|0|0|0|0|0|1|1|0|0|1|0|1|0|1|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||M3||0||M2||0||M1||0||M0||
|Reset|0|0|1|1|0|0|1|0|0|0|0|1|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—<br>30-28|Reserved|
|—<br>27<br>—<br>26-24<br>M6|Reserved<br>Master 6 Priority<br>This field sets the arbitration priority for this port on the associated slave port.<br>000b - This master has level 1 or highest priority when accessing the slave port.<br>001b - This master has level 2 priority when accessing the slave port.<br>010b - This master has level 3 priority when accessing the slave port.<br>011b - This master has level 4 priority when accessing the slave port.<br>100b - This master has level 5 priority when accessing the slave port.<br>101b - This master has level 6 priority when accessing the slave port.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

384 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

##### Table continued from the previous page... 

|Field|Function<br>110b - This master has level 7 priority when accessing the slave port.<br>111b - This master has level 8 or lowest priority when accessing the slave port.|
|---|---|
|23<br>—|Reserved|
|22-20<br>M5|Master 5 Priority<br>This field sets the arbitration priority for this port on the associated slave port.<br>000b - This master has level 1 or highest priority when accessing the slave port.<br>001b - This master has level 2 priority when accessing the slave port.<br>010b - This master has level 3 priority when accessing the slave port.<br>011b - This master has level 4 priority when accessing the slave port.<br>100b - This master has level 5 priority when accessing the slave port.<br>101b - This master has level 6 priority when accessing the slave port.<br>110b - This master has level 7 priority when accessing the slave port.<br>111b - This master has level 8 or lowest priority when accessing the slave port.|
|19<br>—|Reserved|
|18-16<br>M4|Master 4 Priority<br>This field sets the arbitration priority for this port on the associated slave port.<br>000b - This master has level 1 or highest priority when accessing the slave port.<br>001b - This master has level 2 priority when accessing the slave port.<br>010b - This master has level 3 priority when accessing the slave port.<br>011b - This master has level 4 priority when accessing the slave port.<br>100b - This master has level 5 priority when accessing the slave port.<br>101b - This master has level 6 priority when accessing the slave port.<br>110b - This master has level 7 priority when accessing the slave port.<br>111b - This master has level 8 or lowest priority when accessing the slave port.|
|15<br>—|Reserved|
|14-12<br>M3|Master 3 Priority<br>This field sets the arbitration priority for this port on the associated slave port.<br>000b - This master has level 1 or highest priority when accessing the slave port.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

385 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||001b - This master has level 2 priority when accessing the slave port.<br>010b - This master has level 3 priority when accessing the slave port.<br>011b - This master has level 4 priority when accessing the slave port.<br>100b - This master has level 5 priority when accessing the slave port.<br>101b - This master has level 6 priority when accessing the slave port.<br>110b - This master has level 7 priority when accessing the slave port.<br>111b - This master has level 8 or lowest priority when accessing the slave port.|
|11|Reserved|
|—<br>10-8<br>M2|Master 2 Priority<br>This field sets the arbitration priority for this port on the associated slave port.<br>000b - This master has level 1 or highest priority when accessing the slave port.<br>001b - This master has level 2 priority when accessing the slave port.<br>010b - This master has level 3 priority when accessing the slave port.<br>011b - This master has level 4 priority when accessing the slave port.<br>100b - This master has level 5 priority when accessing the slave port.<br>101b - This master has level 6 priority when accessing the slave port.<br>110b - This master has level 7 priority when accessing the slave port.<br>111b - This master has level 8 or lowest priority when accessing the slave port.|
|7<br>—|Reserved|
|6-4<br>M1<br>3|Master 1 Priority<br>This field sets the arbitration priority for this port on the associated slave port.<br>000b - This master has level 1 or highest priority when accessing the slave port.<br>001b - This master has level 2 priority when accessing the slave port.<br>010b - This master has level 3 priority when accessing the slave port.<br>011b - This master has level 4 priority when accessing the slave port.<br>100b - This master has level 5 priority when accessing the slave port.<br>101b - This master has level 6 priority when accessing the slave port.<br>110b - This master has level 7 priority when accessing the slave port.<br>111b - This master has level 8 or lowest priority when accessing the slave port.<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

386 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|2-0|Master 0 Priority|
|M0|This field sets the arbitration priority for this port on the associated slave port.|
||000b - This master has level 1 or highest priority when accessing the slave port.<br>001b - This master has level 2 priority when accessing the slave port.<br>010b - This master has level 3 priority when accessing the slave port.<br>011b - This master has level 4 priority when accessing the slave port.<br>100b - This master has level 5 priority when accessing the slave port.<br>101b - This master has level 6 priority when accessing the slave port.|
||110b - This master has level 7 priority when accessing the slave port.<br>111b - This master has level 8 or lowest priority when accessing the slave port.|



#### 11.5.1.3 Control Register (CRS0 - CRS7) 

##### Offset 

|Register|Offset|
|---|---|
|CRS0|10h|
|CRS1|110h|
|CRS2|210h|
|CRS3|310h|
|CRS4|410h|
|CRS5|510h|
|CRS6|610h|
|CRS7|710h|



##### Function 

These registers control several features of each slave port and must be accessed using 32-bit accesses. After CRSn[RO] is set, the PRSn can only be read; attempts to write to it have no effect and result in an error response. 

~~<mark>NOTE</mark>~~ 

See the chip-specific crossbar information for the reset value of this register. 

Not all HPE n fields may be active. See the chip-specific crossbar information for which masters support master high-priority elevation. Setting a field corresponding to a master that does not support master high-priority elevation has no effect. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

387 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/011_Crossbar_Switch_-AXBS-/S32K3XXRM_数据表.pdf-0388-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RO  0 0<br>HLP  HPE6  HPE5  HPE4  HPE3  HPE2  HPE1  HPE0<br>W 1<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0<br>ARB  PCTL  PARK<br>W<br>Reset 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Read Only|
|RO|Forces the PRSn and CRSn registers to be read-only. After being set, only a hardware reset clears this field.<br>0b - The CRSn and PRSn registers are writeable<br>1b - The CRSn and PRSn registers are read-only and cannot be written (attempted writes have<br>no effect on the registers and result in a bus error response).|
|30<br>HLP|Halt Low Priority<br>This field sets the initial arbitration priority for low power-mode requests . Setting this bit will not affect<br>the ,request for low power-mode from attaining highest priority after it has control of the slave ports.<br>0b - The low-power mode request has the highest priority for arbitration on this slave port.<br>1b - The low-power mode request has the lowest initial priority for arbitration on this slave port.|
|29-24<br>—|Reserved|
|23|Reserved|
|—||
|22<br>HPE6|High Priority Elevation 6<br>This field enables master high-priority elevation for master 6, on this slave port. If enabled, the master is<br>able to elevate its priority to the highest.<br>0b - Master high-priority elevation for master 6. is disabled on this slave port.<br>1b - Master high-priority elevation for master 6. is enabled on this slave port.|
|21|High Priority Elevation 5|
|HPE5|This field enables master high-priority elevation for master 5,on this slave port. If enabled, the master is<br>able to elevate its priority to the highest.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

388 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Master high-priority elevation for master 5. is disabled on this slave port.<br>1b - Master high-priority elevation for master 5. is enabled on this slave port.|
|---|---|
|20<br>HPE4|High Priority Elevation 4<br>This field enables master high-priority elevation for master 4,on this slave port. If enabled, the master is<br>able to elevate its priority to the highest.<br>0b - Master high-priority elevation for master 4. is disabled on this slave port.<br>1b - Master high-priority elevation for master 4. is enabled on this slave port.|
|19<br>HPE3|High Priority Elevation 3<br>This field enables master high-priority elevation for master 3,on this slave port. If enabled, the master is<br>able to elevate its priority to the highest.<br>0b - Master high-priority elevation for master 3. is disabled on this slave port.|
||1b - Master high-priority elevation for master 3. is enabled on this slave port.|
|18<br>HPE2|High Priority Elevation 2<br>This field enables master high-priority elevation for master 2, on this slave port. If enabled, the master is<br>able to elevate its priority to the highest.<br>0b - Master high-priority elevation for master 2. is disabled on this slave port.<br>1b - Master high-priority elevation for master 2. is enabled on this slave port.|
|17|High Priority Elevation 1|
|HPE1|This field enables master high-priority elevation for master 1 on this slave port. If enabled, the master is<br>able to elevate its priority to the highest.<br>0b - Master high-priority elevation for master 1. is disabled on this slave port.<br>1b - Master high-priority elevation for master 1. is enabled on this slave port.|
|16<br>HPE0|High Priority Elevation 0<br>This field enables master high-priority elevation for master 0,on this slave port. If enabled, the master is<br>able to elevate its priority to the highest.<br>0b - Master high-priority elevation for master 0. is disabled on this slave port.<br>1b - Master high-priority elevation for master 0. is enabled on this slave port.|
|15-10<br>—|Reserved|
|9-8|Arbitration Mode|
|ARB|This field selects the arbitration policy for the slave port.<br>00b - Fixed priority|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

389 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||01b - Round-robin (rotating) priority<br>10b - Reserved<br>11b - Reserved|
|7-6<br>—|Reserved|
|5-4|Parking Control|
|PCTL|This field determines the slave port's parking control. The low-power park feature results in an overall<br>power savings if the slave port is not saturated; however, this forces an extra latency clock when any<br>master tries to access the slave port when not in use because it is not parked on any master.<br>00b - When no master makes a request, the arbiter parks the slave port on the master port<br>defined by the PARK bit field.<br>01b - When no master makes a request, the arbiter parks the slave port on the last master to be<br>in control of the slave port.|
||10b - Low-power park. When no master makes a request, the slave port is not parked on a<br>master and the arbiter drives all outputs to a constant safe state.<br>11b - Reserved|
|3|Reserved|
|—<br>2-0|Park|
|PARK|This field determines which master port the current slave port parks on when no masters are actively making<br>requests and the PCTL bits are cleared.|
||~~NOTE~~|
||Select only master ports that are present on the chip. Otherwise, undefined behavior<br>might occur.|
||000b - Park on master port M0|
||001b - Park on master port M1|
||010b - Park on master port M2<br>011b - Park on master port M3|
||100b - Park on master port M4<br>101b - Park on master port M5<br>110b - Park on master port M6<br>111b - Park on master port M7|



## 11.6 Glossary 

AMBA Advanced Microcontroller Bus Architecture 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

390 / 4640 

NXP Semiconductors 

Crossbar Switch (AXBS) 

IDLE A type of transfer that a master uses when it does not want to perform a data transfer ID Master port number 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

391 / 4640 

