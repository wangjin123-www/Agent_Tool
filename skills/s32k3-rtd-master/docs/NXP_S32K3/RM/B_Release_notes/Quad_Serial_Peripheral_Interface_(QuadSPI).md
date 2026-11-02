NXP Semiconductors 

Release notes 

# B.74 Ethernet Media Access Controller (EMAC) 

B.74.1 Chip-specific EMAC information changes 

No substantial content changes. 

## B.74.2 ENET_Controller module changes 

- MAC_VLAN_HASH_TABLE register: Updated description as 'The upper four bits of the calculated CRC value are used to index the contents of the VLAN hash table' 

- MAC_VLAN_Tag.DOVLTC: Added 'The VLAN filter is bypassed when VLAN type ... VLAN type in the VLAN filter' 

# B.75 Gigabit Ethernet Media Access Controller (GMAC) 

B.75.1 Chip-specific GMAC information changes 

No substantial content changes. 

## B.75.2 GMAC module changes 

- Added new chapter for S32K358 variant. 

# B.76 Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

B.76.1 Chip-specific LPUART information changes 

No substantial content changes. 

## B.76.2 LPUART module changes 

No substantial content changes. 

# B.77 Quad Serial Peripheral Interface (QuadSPI) 

B.77.1 Chip-specific QuadSPI information changes 

No substantial content changes. 

## B.77.2 QuadSPI module changes 

- Removed the phrase ",and this depends on the configuration of RBCT[RXBRD]" in Flash memory read section 

- Changed the figure title to "Data strobe functionality in SDR mode for read operation" in Figure 478. 

- Added a Note in the Figure 471. 

- Added a Note:The IOs are driven from QuadSPI as per the number of pads configured for ongoing phase for the Figure 471 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4635 / 4640 

NXP Semiconductors 

Release notes 

- Removed 2nd and 3rd Note in the Figure 471 

- Updated Figure 471 with Note1. 

- Changed "DLLCRL"to "DLLCRB" in the section Dummy Pad loopback 

- Changed the content for high and low frequency delay chain manual programming with additional content with "DLLCR[FREQEN]" and "or DLLCRB[SLV_DLY_COARSE]" in the section Dummy Pad loopback 

- Changed the variable "tDel,total" to "ttotal_delay" in the section Basic description under the topic "Sampling of serial flash memory input data" 

- Updated the description of the Master Read Command (MRC) 

- Updated the description of the Master Timeout (MTO) 

- Updated the description of the Master Global Configuration (MGC) 

- Updated Figure 470 

- Added the parameterised phrase "or using AHB (64-bit width interface)" in the section Features 

- Updated the Register file for SR register description in the section SR[RXFULL] 

- Updated the Register file for MCR register description for 0b in the section MCR[SWRSTSD] 

- Updated the Register file for MCR register description of 0b bit in the section MCR[SWRSTHD] 

- Added new image for the Figure 470 

- Updated the Register file for SR register description in the section SR[TXWA] 

- Updated the Register file for RSER register description in the section RSER[CRCAIE] 

- Updated the Register file for FR register description in the section FR[CRCAEF ] 

- Updated the Instruction set entry for the CMD instruction in the Programmable sequence engine section 

- Updated the Instruction set entry for the DATA_LEARN instruction in the Programmable sequence engine section for Operand[6:0] 

- Updated the LUT section statement for Reset Sequence Table for more clarity in LUT 

- Updated the description for Flash Programming memory section for better clarity in Flash memory programming 

- Added the description for Flash memory read section in 2nd bullet point of "A read access to the external serial flash memory device can be triggered in two different ways:" in Flash memory read 

- Added the description for "Byte ordering of serial flash memory read data" topic in the section Byte ordering of serial flash memory read data 

- Updated the description for 2nd Note in the topic "DQS sampling method" in DQS sampling method 

- Removed the sentence "Master should ensure that it completes the programming sequence for flash access request (write SFAR and IPCR with SEQID) so that target queue is not left after writing SFAR or IPCR without the SEQID." from the section MDAD. and placed it after "If IPCR is written before SFAR then it will result in IPS transfer error." in the section MDAD checks 

- Changed the description of the "Data masking during write list" from the section HyperRAM support. and replaced it with new descrition as per SMEs inputs with the list "Programming considerations for HyperRAM support". 

- Tagged the "CK2_DCARS_FB" with new expression in MCR register description section 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4636 / 4640 

