NXP Semiconductors 

# Chapter 34 Security Overview 

## 34.1 Introduction 

This chip has a comprehensive set of customer-configurable security features designed to protect code and data from unauthorized access. The content of this section is for non-secure operation only. Contact your NXP representative for details if you need secure operation. 

## 34.2 Security features 

S32K3xx: 

- Exceeds the EVITA- full<sup>[5]</sup> functionality and offers high performance for edge nodes applications. 

- Bases its chip censorship on the life cycle model. Access to chip code and data becomes progressively more restricted as the chip matures through a defined set of life cycle steps. 

- Offers these memory security features: 

   - NVM censorship support 

   - Debug password protection 

   - OTP flash memory areas 

- Supports a unique ID—The chip has a unique ID stored in an OTP flash memory area. Any core on the chip can read this unique ID. 

- Includes HSE_B, which is a dedicated security system providing: 

   - A processor core 

   - Dedicated SRAM 

   - Symmetric Hardware Accelerator 

   - Asymmetric Hardware Accelerator 

   - True Random Number Generator (TRNG) 

   - Pseudo Random Number Generator (PRNG) 

   - Exclusive access to secure areas of the chip's flash memory 

   - OTA : In Field Secure Code/Data updates 

~~<mark>NOTE</mark>~~ 

Refer Security Reference Manual and Firmware Reference Manual for the details on OTA. 

Also, HSE_B runs NXP firmware independently from the main chip processor cores and can implement advanced security and monitoring functions. 

- Supports a secure debugger interface. 

- Provides boot modes: 

- [5] EVITA was a European research project existing from 2008 to 2011. There is no standard or a specification to test compliancy. However, HSE_B meets the common expectations often described in the industry as EVITA Full and exceeds them in these cases: 

   - HSE_B supports up to AES-256 instead of AES-128 

   - HSE_B supports up to ECC-521 instead of ECC-256 

   - HSE_B supports SHA-2/Miyaguchi-Preneel instead of Whirlpool 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1037 / 4640 

NXP Semiconductors 

Security Overview 

   - Trusted and secure boot support 

   - Handshake that supports BAF 

- Monitors operating conditions to maximize tampering resistance. 

- Includes basic debugger restrictions (on and off via censorship mode). 

When HSE_B detects a security failure, it moves the chip to a secure state. The chip secure states comply with the chip safe states. You enter a safe state as reset when there are security errors leading to reset. Moreover, if the chip stays in Run mode and the lifecycle moves to the IN_FIELD phase in reaction to errors, the safety application can continue running without glitches. 

## 34.3 Security information 

Chip security feature details are published in the HSE firmware reference manual and HSE service interface manual. Contact your NXP sales representative for more information. 

## 34.4 Glossary 

AES Advanced encryption standard BAF Boot assist flash ECC Elliptic curve cryptography EVITA E-safety vehicle intrusion protected applications NVM Nonvolatile memory OTP One-time programmable 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1038 / 4640 

