NXP Semiconductors 

Release notes 

# B.32 Reset Generation Module (MC_RGM) 

## B.32.1 Chip-specific MC_RGM information changes 

No substantial content changes. 

## B.32.2 MC_RGM module changes 

- Added following note in sectionReset state machine: See chip-specific MC_RGM information for chip-specific reset sequence details. 

- Added following note in DES[F_POR] field: All reset status in the FES and DES registers must be ignored at power up if this field is set. 

- Removed the following content fromFunctional reset entry timer: See the chip-specific section for the default value of timeout value and the details on the chip behavior in case of functional reset entry timer timeout. 

- Added section: Alternate event generation. 

- Removed the following statement from RESET_B pin assertion and pin safe state control: See STCU2 chapter for more details on its usage. 

- Added following note in Functional reset escalation: Functional counter increments for each reset source for which escalation is enabled. For details, see "Reset sources" table in the Reset chapter. 

- Added following note in Destructive reset escalation: Desctructive counter increments for each reset source for which escalation is enabled. For details, see "Reset sources" table in the Reset chapter. 

# B.33 POR_WDG module changes 

No substantial content changes. 

# B.34 Security overview changes 

No substantial content changes. 

# B.35 HSE_B module changes 

No substantial content changes. 

# B.36 DCF module changes 

- Remove the sections Spreaded triple voting and Second write check. 

- Remove a row UTEST DCF start record from the table Integration of DCF information. 

# B.37 Chip-specific DCM information changes 

- Added Read Only GPR On Destructive Reset Register (DCMROD8). 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4625 / 4640 

