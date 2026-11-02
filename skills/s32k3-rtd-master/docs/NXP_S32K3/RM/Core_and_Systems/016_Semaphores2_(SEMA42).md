NXP Semiconductors 

# Chapter 16 Semaphores2 (SEMA42) 

## 16.1 Chip-specific SEMA42 information 

### 16.1.1 SEMA42 instance and configuration 

This chip has up to one instance of SEMA42. See the following table for availability of SEMA42 instance across S32K3xx product series. 

Table 54. SEMA42 instance 

|Instance|S32K322/S32K342/S32K314/S32K324/S32K344/S32K358|S32K311/S32K312|
|---|---|---|
|SEMA42|Yes|No|



See "Chip-specific XRDC information" for the domain ID of each master on the S32K3xx product series. The following table shows the number of domains per chip: 

Table 55. Number of domains 

|Chip|Number of domains|
|---|---|
|S32K311|2|
|S32K312|2|
|S32K322|3|
|S32K342|2|
|S32K314|2|
|S32K324|3|
|S32K344|2|
|S32K328|3|
|S32K338|4|
|S32K348|2|
|S32K358|3|



## 16.2 Introduction 

SEMA42 is a memory-mapped module that provides robust hardware support needed in multi-core systems for implementing semaphores and provides a simple mechanism to achieve "lock and unlock" operations via a single - write access. The hardware semaphore module provides hardware-enforced gates as well as other useful system functions related to the gating mechanisms. 

### 16.2.1 Multi-core programming: software gates 

Multi-processor systems require a function that can be used to safely and easily provide a locking mechanism for system software to control access to shared data structures, shared hardware resources, and so on. The software uses the gating mechanisms to serialize (and synchronize) accesses to shared data and/or resources to prevent race conditions and preserve memory coherency between different processes and domains. 

Consider the following description of a typical use-case: Domain X enters a section of code where shared data values are to be updated. The domain must first acquire a semaphore. Think of this as the locking (or closing) of a software gate. After the gate locks, a properly-architected software system does not allow other processes (or domains) to execute the same code segment 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

516 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 

or modify the shared data structure protected by the gate. In other words, the system locks out other processes/domains. Many software implementations include a spin-wait loop within the lock function until the gate locks. After domain X obtains the lock, domain X continues execution and updates the data values protected by the particular lock. After domain X completes the updates, it unlocks (or opens) the software gate, allowing other processes/domains access to the updated data values. 

A correctly-implemented system solution must follow these important rules: 

- A gate variable must protect all writes to shared data values or shared hardware resources. 

- After a domain locks a gate, the system must block other processes/domains from accessing the shared data or resources. Software conventions enforce this. 

- The domain that locks a particular gate is the only domain that can open (unlock) that gate. 

Information in the hardware gate identifying the locking domain can be extremely useful for system-level debugging. 

### 16.2.2 Features 

SEMA42 implements hardware-enforced semaphores as an IPS-mapped slave peripheral device. The feature set includes: 

- Support for 16 hardware-enforced gates in a multi-domain configuration that supports up to 15 domains. In this chapter, dmX represents domain X. 

— Gates appear as a 16-entry byte-size array with read and write accesses. 

   - ◦Domains lock gates by writing "domainID_number+1" to the appropriate gate and must read back the gate value to verify that the lock operation succeeded. 

   - ◦After the gate locks, the locking domain unlocks the gate by writing zeroes. 

- Each hardware gate appears as a 16-state, 4-bit state machine. 

   - ◦16-state implementation 

If gate = 0h, then state = unlocked 

if gate = 1h, then state = locked by domain (master) 0 if gate = 2h, then state = locked by domain (master) 1 

if gate = Fh, then state = locked by domain (master) 14 

      - ◦SEMA42 uses the logical domain number and the specified data patterns as reference attributes to validate all write operation. 

      - ◦After a gate locks, the locking domain must unlock the gate by writing zeroes. 

   - Support for secure reset mechanisms to clear the contents of individual gates, as well as a clear-all capability 

- Memory-mapped slave peripheral that offers programming-model accesses 

The following figure shows a simplified SEMA42 block diagram. In the diagram, the register blocks named gate0, gate1,…, gate (n-2) and gate (n-1) include the finite state machines implementing the semaphore gates. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

517 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/016_Semaphores2_-SEMA42-/S32K3XXRM_数据表.pdf-0518-02.png)


<!-- Start of picture text -->
4 did<br>= =<br>domainID_eq_dm{0,1, ..., 14} 32 peripheral bus wdata<br>= = =<br>wdata_dm_{unlock, dm[0-14]_lock} peripheral addr<br>decode<br>gate0 gate1 gate2 gate3<br>control<br>gate(n-4) gate(n-3) gate(n-2) gate(n-1)<br>mux<br>32 peripheral rdata<br>Peripheral Bus<br><!-- End of picture text -->

Figure 35. SEMA42 block diagram 

## 16.3 Functional description 

This section describes more about the SEMA42 functional operation and specific details of the state machines of the GATEn registers. 

As described previously, each of the GATEn registers implements a 4-bit, 16-state machine. The following figure shows a simplified diagram of the state transitions for each gate. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

518 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/016_Semaphores2_-SEMA42-/S32K3XXRM_数据表.pdf-0519-02.png)


<!-- Start of picture text -->
reset<br>1<br>idle<br>0000 ~((did == dm0) & (wdata == dm0_lock))<br>&~((did == dm1) & (wdata == dm1_lock))<br>& ...<br>2 &~((did == dmE) & (wdata == dmE_lock))<br>did == dm0 did == dmE<br>& (wdata == dm0_lock) & (wdata == dmE_lock)<br>3 4<br>dm0_lock .... dmE_lock<br>0001 1111<br>5 7<br>did != dm0 (wdata != unlock) did != dmE (wdata != unlock)<br>6 8<br>did == dm0 & (wdata == unlock) did == dmE & (wdata == unlock)<br><!-- End of picture text -->

Figure 36. GATEn state machine 

In the figure above, "did" is the domain identifier and "dm" is the domain number. The domain number identifies core domain X (dmX). Thus, for example, "dmE" represents domain 14 (E in hexadecimal). The platform passes the domain number to SEMA42. 

The following table defines the GATEn state transitions. 

Table 56. GATEn state transitions 

|Current state|Next state|Transition|Description|
|---|---|---|---|
|–|idle|1|Any reset, whether a system reset or a software-initiated gate reset,<br>unconditionally forces the gate into the idle state.|
|idle|idle|2|Unless a write of the appropriate lock value from the corresponding<br>domain occurs, the gate remains in the idle state.|
|idle|dm0_lock|3|When domain 0h initiates a write of the dm0_lock data value, the gate<br>transitions into the dm0_lock state.|
|idle|dmE_lock|4|When domain Eh initiates a write of the dmE_lock value, the gate<br>transitions into the dmE_lock state.|
|dm0_lock|dm0_lock|5|When in this state, the gate remains here if any attempted write is not<br>from domain 0h with the unlock data value.|
|dm0_lock|idle|6|The gate returns to the idle (unlocked) state after a write from domain 0h<br>with the unlock data value occurs.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

519 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 

Table 56. GATEn state transitions (continued) 

|Current state|Next state|Transition|Description|
|---|---|---|---|
|dmE_lock|dmE_lock|7|When in this state, the gate remains here if any attempted write is not<br>from domain Eh with the unlock data value.|
|dmE_lock|idle|8|The gate returns to the idle (unlocked) state after a write from domain Eh<br>with the unlock data value occurs.|



SEMA42 uses these gate data values: 

- The lock data value is (domain number) + 1. 

- The unlock data value is 00h. 

## 16.4 Memory map/register definition 

You can access these registers only in Supervisor mode. User accesses terminate with an error. 

### 16.4.1 SEMA42 register descriptions 

#### 16.4.1.1 SEMA42 memory map 

SEMA42 base address: 4046_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h - Fh|Gate Register (GATE0 - GATE15) <sup>1</sup>|8|RW|00h|
|42h|Reset Gate Read (RSTGT_R)|16|RO|0000h|
|42h|Reset Gate Write (RSTGT_W)|16|WO|See<br>description|



1. In this array, the index and offset values of the registers do not increment in direct alignment. For details, see the register description. 

#### 16.4.1.2 Gate Register (GATE0 - GATE15) 

##### Offset 

For n = 0 to 15: 

|Register|Offset|
|---|---|
|GATEn|0h + (n + 3 - 2 × (n mod 4))|



##### Function 

SEMA42 implements each semaphore gate in a 4-bit finite state machine, right-justified in a byte data structure. The hardware uses the logical domain-identifier number in conjunction with the data patterns to validate all attempted write operations. Only domain masters can modify the gate registers. After a gate locks, only the locking domain must open (unlock) the gate. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

520 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 

You can read multiple gate values in a single access. However, you can update only a single gate at a time, via a write operation. If you attempt to write a byte-wide value that is neither the unlock value (00h) nor the appropriate lock value (domainID_number + 1), SEMA42 considers this as "no operation" and does not change any gate state. Attempts to write multiple gates in a single-aligned access with a size larger than 8 bits (byte) generate an error termination and do not allow any gate state changes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/016_Semaphores2_-SEMA42-/S32K3XXRM_数据表.pdf-0521-04.png)


<!-- Start of picture text -->
Bits 7 6 5 4 3 2 1 0<br>R 0<br>GTFSM<br>W<br>Reset 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|7-4<br>—|Reserved|
|3-0|Gate finite state machine|
|GTFSM|The state of the gate reflects the last domain that locked it. This can be useful during system debug.<br>The hardware gate has a 16-state implementation, defined as:<br>0000b - The gate is unlocked (free).<br>0001b - Domain 0 locked the gate.<br>0010b - Domain 1 locked the gate.<br>0011b - Domain 2 locked the gate.<br>0100b - Domain 3 locked the gate.<br>0101b - Domain 4 locked the gate.<br>0110b - Domain 5 locked the gate.<br>0111b - Domain 6 locked the gate.|
||1000b - Domain 7 locked the gate.<br>1001b - Domain 8 locked the gate.<br>1010b - Domain 9 locked the gate.<br>1011b - Domain 10 locked the gate.<br>1100b - Domain 11 locked the gate.<br>1101b - Domain 12 locked the gate.<br>1110b - Domain 13 locked the gate.|
||1111b - Domain 14 locked the gate.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

521 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 

#### 16.4.1.3 Reset Gate Read (RSTGT_R) 

##### Offset 

|Register|Offset|
|---|---|
|RSTGT_R|42h|



##### Function 

This section and Reset Gate Write (RSTGT_W) describe the same register. This section describes the general operation of the register and also shows how the register fields appear when you read the register. Reset Gate Write (RSTGT_W) shows how the register fields appear when you write to the register. 

The intent of the hardware gate implementation is to specify a protocol where the locking domain must unlock the gate. However, some systems may require a reset function to re-initialize the state of any gate(s) without requiring a system-level reset. To support this special gate reset requirement, SEMA42 implements a secure reset mechanism that allows you to initialize a hardware gate (or all the gates) by following a specific dual-write access pattern. The secure-gate reset: 

- Uses a technique similar to that required for the servicing of a software watchdog timer 

- Requires two consecutive writes with pre-defined data patterns from the same domain 

You must do this to force the clearing of the specified gate(s). The required access pattern as follows: 

1. A domain performs a 16-bit write to the RSTGT memory location. The most significant byte (RSTGT_W[RSTGDP]) must be E2h. The value of least significant byte is irrelevant for this reference and can be anything. 

2. The same domain then performs a second 16-bit write to the RSTGT location. For this write, the upper byte (RSTGT_W[RSTGDP]) is the logical complement of the first data pattern (1Dh) and the lower byte (RSTGT_W[RSTGTN]) specifies the gate(s) to be reset. This gate field can specify a single gate or all gates to be cleared. If the same domain writes incorrect data on the second access or another domain performs the second write access, SEMA42 aborts the special gate reset sequence and does not assert an error signal. 

3. Reads of the RSTGT location return information on the 2-bit reset state machine (RSTGT_R[RSTGSM]) that implements these functions: 

   - The domain performing the reset (RSTGT_R[RSTGMS]) 

   - The last-cleared gate number(s) (RSTGT_R[RSTGTN]) 

Reads of the RSTGT register do not affect the secure-reset finite state machine in any manner. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/016_Semaphores2_-SEMA42-/S32K3XXRM_数据表.pdf-0522-18.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RSTGSM  RSTGMS  RSTGTN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15-14|ROZ|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

522 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|ROZ|This field always returns the value 0 when you read it.|
|13-12|Reset gate finite state machine|
|RSTGSM|Reads of the RSTGT register return the encoded state machine value. RSTGSM = 10b is valid for only a<br>single machine cycle, so a read can never return this value. SEMA42 maintains the reset state machine in<br>a 2-bit, 3-state implementation, defined as follows:<br>00b - Idle, waiting for the first data pattern write.<br>01b - Waiting for the second data pattern write<br>10b - The 2-write sequence has completed. Generate the specified gate reset(s). After the reset is<br>performed, this machine returns to the idle (waiting for first data pattern write) state.<br>11b - This state encoding is never used and therefore reserved.|
|11-8|Reset gate domain|
|RSTGMS|This field records the logical number of the domain performing the gate reset function. The logical number<br>is the domain number. This domain number is determined by the XRDC's Master Domain Assignment<br>Controller (XRDC_MDAC). To succeed, this function requires that the same domain initiate the two<br>consecutive writes to this register. SEMA42 updates the field each time a write to this register occurs.|
|7-0|Reset gate number|
|RSTGTN|This field specifies the specific hardware gate to be reset. The second write updates this field.<br>If RSTGTN < 64, SEMA42 resets the single gate defined by RSTGTN. Otherwise, SEMA42 resets all<br>the gates.|



#### 16.4.1.4 Reset Gate Write (RSTGT_W) 

##### Offset 

|Register|Offset|
|---|---|
|RSTGT_W|42h|



##### Function 

This section describes how the RSTGT fields appear when the register is written. See Reset Gate Read (RSTGT_R) for the description of the register's overall operation and how the register fields appear when you read the register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/016_Semaphores2_-SEMA42-/S32K3XXRM_数据表.pdf-0523-10.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W RSTGDP  RSTGTN<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br><!-- End of picture text -->

1. Reset value is not applicable for writes. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

523 / 4640 

NXP Semiconductors 

Semaphores2 (SEMA42) 

##### Fields 

|Field|Function|
|---|---|
|15-8|Reset gate data pattern|
|RSTGDP|You access this field with the specified data patterns on the two consecutive writes to enable the gate-reset<br>mechanism. For the first write, RSTGDP must be E2h. For the second write, RSTGDP must be 1Dh.|
|7-0|Reset gate number|
|RSTGTN|This field specifies the specific hardware gate to be reset. The second write updates this field.|
||If RSTGTN < 64, SEMA42 resets the single gate defined by RSTGTN. Otherwise, SEMA42 resets all<br>the gates.|



## 16.5 Glossary 

IPS Protocol used for peripheral accesses to the programming model 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

524 / 4640 

