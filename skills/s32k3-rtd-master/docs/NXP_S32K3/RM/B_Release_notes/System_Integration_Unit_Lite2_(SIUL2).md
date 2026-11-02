NXP Semiconductors 

Release notes 

## B.7.2 MSCM module changes 

- Added registers ENEDC1 and IAHBCFGREG 

- Made changes to the CPXTYPE, CPXNUM, CP2TYPE, CP2NUM, CP2REV, CP2CFG0, CP2CFG1, CP2CFG2, CP2CFG3, IRCP0ISR0, IRCP0IGR0, ENEDC, ENEDC1, IAHBCFGREG, IRSPRC0, and XN_CTRL registers. 

- Changed the reset values of these registers: CPXCFG0 to 0602_0604h, CP0CFG0 to 0602_0604h, CP1CFG0 to 0602_0604h, and XN_CTRL to 4000_0000h. 

- Marked bit positions 30 and 31 of the ENEDC register as "reserved." 

- Added fields "Soft lock" and "Hard lock" to the XN_CTRL register. 

# B.8 Virtualization Wrapper (VIRT_WRAPPER) 

## B.8.1 Chip-specific VIRT WRAPPER information changes 

No substantial content changes. 

## B.8.2 Virt_Wrapper changes 

- Updated the note from "Access to reserved spaces outside the register bank generates the transfer error. However, access to the reserved spaces within the register bank does not have any effect" to "Access to reserved spaces outside the register bank and holes (unimplemented registers) within register bank generates the transfer error.". 

- Added the note "Any master can access holes (unimplemented registers) of SIUL2 through PDAC0." for REG_A and REG_B. 

- Corrected the syntax to show the reserve RW Implemented hole bits within the registers REG_A and REG_B using MSCR_MAPPED parameter for REG_A and REG_B. 

- Changed from PDAC to PDAC slot as applicable throughout the document. 

- Added a note, "PDAC and PDAC slot are interchangeable terms." in Glossary. 

- Updated "10 - Reserved" as "10 - SIUL2_VIRTWRAPPER_PDAC4" throughout the document. 

# B.9 System Integration Unit Lite2 (SIUL2) 

## B.9.1 Chip-specific SIUL2 information changes 

No substantial content changes. 

## B.9.2 SIUL2 module changes 

- In the note "For the array of 16-bit registers PGPDOn and PGPDIn": rephrased the second bullet-item. 

- Added field values 'Low' and 'High' for PGPDOn and PGPDIn registers. 

- In External interrupt initialization added a new step 1 and added a note "When you chose external interrupt inputs for ...". 

- Changed access type of reserved field from ROZ to RO in IFCPR and IFMCRn registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4620 / 4640 

