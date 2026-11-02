NXP Semiconductors 

Release notes 

## B.49.2 ERM module changes 

- Updated the description of the SR registers. 

- Added following note in the "ERM register descriptions" section: To access the channel registers, corresponding channel clocks must be enabled. 

# B.50 Fault Collection and Control Unit (FCCU) 

## B.50.1 Chip-specific FCCU information changes 

No substantial content changes. 

## B.50.2 FCCU module changes 

- Note "Software reset of FCCU by MC_RGM_PRST5[FCCU_RST] bit is optional since FCCU registers are not initialized during functional reset. MC_RGM_PRST5[FCCU_RST] has the same effect on FCCU as power on reset. If the bit is activated, it can change the state of the error pin, if the current state of the pin is different from default." removed from topic "Use cases and limitations". 

- Reset interface topic moved into chip specific section. 

- The equation changed from "Tmin = 250 μs + DELTA_T to "Tmin = (250us + DELTA_T) * (SAFE_CLK_FREQ/CLKSAFE freq). 

# B.51 SELFTEST_GPR module changes 

- Information added for different K3xx variants (K342, K312 and K311). 

- Added note in Introduction section. 

# B.52 Self-Test Control Unit (STCU2) 

## B.52.1 Chip-specific STCU2 information changes 

No substantial content changes. 

## B.52.2 STCU2 module changes 

- In Example: Multi-phase BIST sequence, changed the BIST number from 38 to 30 for phase 0. 

- Removed MTR from the function of "MBIST interface" in Table 258. 

# B.53 Register Protection (REG_PROT) 

## B.53.1 Chip-specific REGPROT information changes 

No substantial content changes. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4628 / 4640 

