NXP Semiconductors 

Release notes 

# B.71 Flexible I/O (FlexIO) 

## B.71.1 Chip-specific FlexIO information changes 

No substantial content changes. 

## B.71.2 FLEXIO module changes 

No substantial content changes. 

# B.72 CAN (FlexCAN) 

## B.72.1 Chip-specific FlexCAN information changes 

- In FlexCAN instances and configuration, added note "The availability of 'Interrupt Masks 3 Register (IMASK3)' and 'Interrupt Flags 3 Register (IFLAG3)' registers for an instance depends upon the number of message buffers..". 

## B.72.2 FlexCAN module changes 

- In Overview, removed the text "See the chip-specific FlexCAN information for the actual number of message buffers configured in the chip". 

- In Features, Overview and , updated the ISO 11898-1 to ISO 11898-1:2015. 

- In Protocol timing, added text "It is the smallest time unit for all configuration values". 

- Updated the ISO 11898-1 to ISO 11898-1:2015 throughout the chapter. 

- In Bus interface added the following registers: 

   - EPRS 

   - ENCBT 

   - EDCBT 

   - ETDC 

# B.73 Synchronous Audio Interface (SAI) 

## B.73.1 Chip-specific SAI information changes 

- Updated Table 485. 

## B.73.2 SAI module changes 

- Updated TCR2[BCI] and RCR2[BCI] with note about enabling buffers. 

- Updated field descriptions: TCSR[FR], TCSR[SR], TCSR[FWDE], TCR1[TFW], TCR5[WNW], TCR5[W0W], TCR5[FBT]. RCSR[FR], RCSR[SR], RCSR[FWDE], RCR1[RFW], RCR3[WDFL], RCR4[FRSZ], RCR4[SYWD], RCR5[WNW], RCR5[W0W], and RCR5[FBT]. 

- In Receive Configuration 5 (RCR5), updated description. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4634 / 4640 

