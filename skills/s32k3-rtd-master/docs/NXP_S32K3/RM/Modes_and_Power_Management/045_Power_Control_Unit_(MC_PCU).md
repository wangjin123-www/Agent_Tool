NXP Semiconductors 

# Chapter 45 Power Control Unit (MC_PCU) 

## 45.1 Introduction 

The power control unit (MC_PCU) is used for initiating a Standby mode entry that reduces the overall chip power consumption. Power can be saved by disconnecting parts of the chip from the power supply. The blocks inside the chip are grouped into multiple parts having this capability, which are called "power domains". 

When a power domain is disconnected from the supply, the power consumption is reduced to zero in that domain. Any status information, such as, power domain is lost. When you reconnect a power domain to the supply voltage, the domain draws an increased current until the power domain reaches its operational voltage. Maximum power saving is achieved by entering the Standby mode. 

After the MC_ME asserts a standby entry request, MC_PCU initiates the power sequence, which is non-retractable and includes the handshake with the chip power management controller. The power-up/down sequences are handled by FSMs to ensure a smooth and safe transition into and out of the Standby mode. Exiting the Standby mode can only be done through a system wakeup event, power-on reset, destructive reset, or a functional reset. 

## 45.2 Power sequence FSM 

MC_PCU implements an FSM to initiate the power sequencing of the Standby mode entry/exit sequence for the chip. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1568 / 4640 

NXP Semiconductors 

Power Control Unit (MC_PCU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/045_Power_Control_Unit_-MC_PCU-/S32K3XXRM_数据表.pdf-1569-02.png)


<!-- Start of picture text -->
standby entry request<br>IDLE<br>MC_ME<br>INTF<br>software low-power UNLOCK<br>entry process<br>Input ISO. active Input ISO inactive<br>INTF SW L<br>LOCK CLOSE<br>Switchable domain supply ON<br>Output ISO. active Output ISO inactive<br>SW H<br>SW OPEN<br>CLOSE<br>PMC in low<br>Switchable domain supply OFF<br>power mode<br>PMC in full<br>FIRC PowerDown performance mode<br>PWR DOWN PWR UP<br>FIRC PowerUp<br>Reset event (Functional/destructive) activated<br>or<br>Wakeup source activated<br>Figure 173. MC_PCU FSM<br>  NOTE<br><!-- End of picture text -->

When destructive reset is asserted from MC_RGM, MC_PCU FSM moves to the IDLE state immediately. Indication 

of this is not shown in the above figure. 

Table 227. MC_PCU FSM transition description 

|State|Name|Exit condition|Signal controlled|Signal monitored|
|---|---|---|---|---|
|IDLE|Idle state|Standby request<br>received from MC_ME|-|-|
|MC_ME software low<br>power entry process|MC_ME software low<br>power entry process|Software entry<br>sequence completed<br>(SW4 process<br>completed)|-|-|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1569 / 4640 

NXP Semiconductors 

Power Control Unit (MC_PCU) 

Table 227. MC_PCU FSM transition description (continued) 

|State|Name|Exit condition|Signal controlled|Signal monitored|
|---|---|---|---|---|
|INTF LOCK|Interface lock state|Input isolation active|Input isolation<br>activation; Switchable<br>power-domain reset|Input isolation active|
|SW OPEN|Switch open state|Output isolation active,<br>Switchable domain<br>supply turned off|Output isolation<br>activation, low power<br>mode request to PMC|Output isolation active,<br>Switchable domain<br>supply|
|PWR DOWN|Power down state|Wakeup/functional<br>reset occurrence|SIRC power down|Wakeup and functional<br>reset|
|PWR UP|Power up state|PMC in full<br>performance mode|-|-|
|SW H CLOSE|Switch H close state|Switchable domain<br>supply turned on|-|Switchable domain<br>supply|
|SW L CLOSE|Switch L close state|Output isolation<br>inactive|Output isolation<br>activation|Output isolation active|
|INTF UNLOCK|Interface unlock|Input isolation inactive|Input isolation<br>activation.|Input isolation active|



## 45.3 Glossary 

FSM Finite state machine 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1570 / 4640 

