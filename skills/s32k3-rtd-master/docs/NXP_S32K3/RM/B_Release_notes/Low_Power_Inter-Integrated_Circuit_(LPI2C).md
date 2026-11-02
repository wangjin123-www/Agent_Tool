NXP Semiconductors 

Release notes 

# B.66 Periodic Interrupt Timer (PIT) 

## B.66.1 Chip-specific PIT information changes 

No substantial content changes. 

## B.66.2 PIT_RTI module changes 

- Updated description of MCR[MDIS]. Changed the sentence “You must write 1 to this field before setting up anything” to “You must ensure that the clock is disabled (MDIS = 1) before configuring PIT. After configuration, user must enable clock (MDIS=0).” 

- Updated Modes of operation to include Debug mode. 

# B.67 Real Time Clock (RTC) 

B.67.1 Chip-specific RTC information changes 

No substantial content changes. 

## B.67.2 RTC module changes 

No substantial content changes. 

# B.68 Low Power Serial Peripheral Interface (LPSPI) 

B.68.1 Chip-specific LPSPI information changes 

No substantial content changes. 

## B.68.2 LPSPI module changes 

- In Master mode, Transmit and command FIFO commands, and Transmit Command (TCR), clarified that LPSPI must be enabled to update command word. 

- Updated Features. 

- Updated Low-power modes 

- Updated Timing parameters. 

- Added a warning on writing data to Clock Configuration (CCR). 

- Moved "SPI bus transfers" content from Transmit and command FIFO commands to subtopic 

- Moved "Circular FIFO" content from Transmit and command FIFO commands to subtopic 

# B.69 Low Power Inter-Integrated Circuit (LPI2C) 

B.69.1 Chip-specific LPI2C information changes 

No substantial content changes. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4632 / 4640 

