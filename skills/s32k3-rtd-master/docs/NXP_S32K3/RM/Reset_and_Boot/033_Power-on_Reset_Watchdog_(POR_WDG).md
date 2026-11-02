NXP Semiconductors 

# Chapter 33 Power-on Reset Watchdog (POR_WDG) 

## 33.1 Introduction 

POR_WDG monitors the chip for stuck or hang scenarios when in reset and standby sequences. It generates a chip power-onreset event to recover the chip in case it remains stuck in reset or standby entry/exit duration for a pre-configured period of time. 

POR_WDG consists of a watchdog counter with a configurable threshold. After the threshold is reached POR_WDG generates a chip power-on-reset event. 

SIRC clocks POR_WDG. 

## 33.2 Features 

- Counter with four possible configurable threshold limits 

- Associate register interfaces to capture the status of input signals 

- Monitors reset, standby entry, and standby exit 

## 33.3 Configurations 

POR_WDG is enabled by default out of reset to actively monitor the chip reset sequence with the default timeout threshold duration. The POR_WDG configuration controls support provisions for enabling or disabling POR_WDG and the counter threshold, as described in the following sections. 

### 33.3.1 Enable/disable configurations 

By default POR_WDG is enabled for reset sequence monitoring, as well as standby entry/exit sequence monitoring for stuck scenarios. The following table describes the controls to enable or disable POR_WDG operation. 

Table 188. POR_WDG enable/disable control 

|POR_WDG monitoring|Default<br>configuration|Enable/disable|
|---|---|---|
|Reset monitoring|Enabled|dcf_client_utest_misc[16]<br>Enables or disables POR_WDG for reset monitoring.<br>0: Disable<br>1: Enable<br>See the DCF clients file attached to this document for details.|
|Standby entry/exit monitoring|Disabled|DCM's DCMRWP1[8]<br>Enables or disables POR_WDG for standby entry/exit monitoring.<br>0: Enable<br>1: Disable<br>See the DCM chapter for details.|



### 33.3.2 Timeout configurations 

POR_WDG supports four configurable counter threshold levels for its counter, as listed in the table below. The default POR_WDG timeout is 25 ms. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1034 / 4640 

NXP Semiconductors 

Power-on Reset Watchdog (POR_WDG) 

Table 189. POR_WDG timeout configuration 

|DCM's DCMRWP1[10]|DCM's DCMRWP1[9]|POR_WDG timeout|
|---|---|---|
|0|0|6.25 ms|
|0|1|12.50 ms|
|1|0|25.00 ms|
|1|1|50.00 ms|



### 33.3.3 Event and status registers 

POR_WDG provides indication of a POR_WDG event along with the status of the chip at the point when the POR_WDG counter overflows. 

POR_WDG event status register: A POR_WDG event is captured in DCM status register DCMROPP4[0]. 

POR_WDG status registers: The status of the chip at the POR_WDG event is captured in DCM status registers DCMROPP1– DCMROPP3. See the DCM chapter for details. 

DCM's DCMROPPn are reset on a POR caused by PMC and are unaffected by a POR_WDG reset. 

## 33.4 Reset sequence monitoring 

### 33.4.1 Introduction 

At power-up POR_WDG is enabled for reset monitoring (DCF record in UTEST Misc can bypass POR_WDG, as described in Table 188). 

On every reset event, POR_WDG starts monitoring the reset sequence (including the functional reset entry sequence, in case of functional reset event). 

If the chip does not exit the reset sequence within the POR_WDG timeout threshold, then POR_WDG initiates a POR sequence to recover the chip from a stuck or hung scenario. You can view the POR_WDG status in DCM's DCMROPPn registers to obtain: 

- Diagnostic status 

- Chip details in the event of a POR_WDG reset 

### 33.4.2 Inactive windows or bypass operation 

POR_WDG monitoring of the reset sequence is inactive in the following conditions: 

- POR_WDG is disabled for reset monitoring by chip configuration in UTEST via dcf_client_utest_misc[16]. See the DCF clients file attached to this document for details. 

- MC_RGM destructive reset escalation (ensures that the chip stays in reset). 

- Extend pin reset by keeping it pressed externally. 

- During selftest, when MC_RGM.RGM_ERCTRL[ERASSERT] is configured as 1. 

### 33.4.3 Windows of operation 

POR_WDG monitors the reset sequence in the following scenarios: 

- Reset pin is active (when chip is in reset, including the functional reset entry sequence). 

- Standby domain functional reset is asserted (when reset pad is pulled up but functional reset is asserted). 

- RUN domain destructive reset is asserted but flash memory is not in Low-Power mode (when RUN domain destructive reset fires unexpectedly in Run mode). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1035 / 4640 

NXP Semiconductors 

Power-on Reset Watchdog (POR_WDG) 

- RUN domain functional reset is asserted but flash memory is not in Low-Power mode (when RUN domain functional reset fires unexpectedly in RUN mode). 

## 33.5 Standby entry/exit sequence monitoring 

### 33.5.1 Introduction 

On every low-power entry or exit event, POR_WDG starts monitoring the low-power sequence (standby entry and standby exit sequence). 

If the chip does not exit the standby entry or exit sequence within the POR_WDG timeout threshold, POR_WDG initiates a POR sequence to recover the chip from the stuck or hung scenario. You can then check the POR_WDG status registers in DCM to check the chip status when POR_WDG raised the POR to the chip. 

### 33.5.2 Inactive windows/bypass operation 

You can configure DCM's DCMRWP1[8] to disable POR_WDG for standby entry and exit sequence monitoring. 

### 33.5.3 Windows of operation 

POR_WDG monitors the standby sequence (standby entry and standby exit) in these scenarios: 

- Standby entry sequence monitoring: Monitoring from main core WFI execution until PMC acknowledges Low-Power mode entry. 

- Standby exit sequence monitoring: Monitoring from wakeup event until the RUN domain reset recovery. 

## 33.6 Glossary 

WFI 

Wait for Interrupt 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1036 / 4640 

