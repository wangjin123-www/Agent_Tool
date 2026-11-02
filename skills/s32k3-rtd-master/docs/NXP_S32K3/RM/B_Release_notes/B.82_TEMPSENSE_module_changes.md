NXP Semiconductors 

Release notes 

## B.78 Ultra Secured Digital Host Controller (uSDHC) 

### B.78.1 Chip-specific uSDHC information changes 

No substantial content changes. 

### B.78.2 uSDHC module changes 

- Added new chapter for S32K358 variant. 

## B.79 Debug changes 

- Removed the following columns from the Table 704: hse_dis_oem, hse_dis_fld, hse_dis_cus, and HSE_DIS_PRE_FA. 

- Updated the reset value of Status (MDMAPSTTS). 

- Added SDAAPRSTCTRL[RSTRELTLCM72]. 

- Removed the information about "HSE_DIS_CR_MCU_PROD" and "HSE Debug" from the Debug across device LifeCycles. 

## B.80 JTAG Controller (JTAGC) 

B.80.1 Chip-specific JTAGC information changes 

No substantial content changes. 

### B.80.2 JTAGC module changes 

No substantial content changes. 

## B.81 JDC module changes 

No substantial content changes. 

## B.82 TEMPSENSE module changes 

No substantial content changes. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4637 / 4640 

NXP Semiconductors 

Legal information 

# Legal information 

## Definitions 

Draft — A draft status on a document indicates that the content is still under internal review and subject to formal approval, which may result in modifications or additions. NXP Semiconductors does not give any representations or warranties as to the accuracy or completeness of information included in a draft version of a document and shall have no liability for the consequences of use of such information. 

## Disclaimers 

Limited warranty and liability — Information in this document is believed to be accurate and reliable. However, NXP Semiconductors does not give any representations or warranties, expressed or implied, as to the accuracy or completeness of such information and shall have no liability for the consequences of use of such information. NXP Semiconductors takes no responsibility for the content in this document if provided by an information source outside of NXP Semiconductors. 

In no event shall NXP Semiconductors be liable for any indirect, incidental, punitive, special or consequential damages (including - without limitation - lost profits, lost savings, business interruption, costs related to the removal or replacement of any products or rework charges) whether or not such damages are based on tort (including negligence), warranty, breach of contract or any other legal theory. 

Notwithstanding any damages that customer might incur for any reason whatsoever, NXP Semiconductors’ aggregate and cumulative liability towards customer for the products described herein shall be limited in accordance with the Terms and conditions of commercial sale of NXP Semiconductors. 

Right to make changes — NXP Semiconductors reserves the right to make changes to information published in this document, including without limitation specifications and product descriptions, at any time and without notice. This document supersedes and replaces all information supplied prior to the publication hereof. 

Applications — Applications that are described herein for any of these products are for illustrative purposes only. NXP Semiconductors makes no representation or warranty that such applications will be suitable for the specified use without further testing or modification. 

Customers are responsible for the design and operation of their applications and products using NXP Semiconductors products, and NXP Semiconductors accepts no liability for any assistance with applications or customer product design. It is customer’s sole responsibility to determine whether the NXP Semiconductors product is suitable and fit for the customer’s applications and products planned, as well as for the planned application and use of customer’s third party customer(s). Customers should provide appropriate design and operating safeguards to minimize the risks associated with their applications and products. 

NXP Semiconductors does not accept any liability related to any default, damage, costs or problem which is based on any weakness or default in the customer’s applications or products, or the application or use by customer’s third party customer(s). Customer is responsible for doing all necessary testing for the customer’s applications and products using NXP Semiconductors products in order to avoid a default of the applications and the products or of the application or use by customer’s third party customer(s). NXP does not accept any liability in this respect. 

Terms and conditions of commercial sale — NXP Semiconductors products are sold subject to the general terms and conditions of commercial sale, as published at http://www.nxp.com/profile/terms, unless otherwise agreed in a valid written individual agreement. In case an individual agreement is concluded only the terms and conditions of the respective agreement shall apply. NXP Semiconductors hereby expressly objects to applying the customer’s general terms and conditions with regard to the purchase of NXP Semiconductors products by customer. 

Export control — This document as well as the item(s) described herein may be subject to export control regulations. Export might require a prior authorization from competent authorities. 

Translations — A non-English (translated) version of a document is for reference only. The English version shall prevail in case of any discrepancy between the translated and English versions. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4638 / 4640 

NXP Semiconductors 

Legal information 

Security — Customer understands that all NXP products may be subject to unidentified vulnerabilities or may support established security standards or specifications with known limitations. Customer is responsible for the design and operation of its applications and products throughout their lifecycles to reduce the effect of these vulnerabilities on customer’s applications and products. Customer’s responsibility also extends to other open and/or proprietary technologies supported by NXP products for use in customer’s applications. NXP accepts no liability for any vulnerability. Customer should regularly check security updates from NXP and follow up appropriately. 

Customer shall select products with security features that best meet rules, regulations, and standards of the intended application and make the ultimate design decisions regarding its products and is solely responsible for compliance with all legal, regulatory, and security related requirements concerning its products, regardless of any information or support that may be provided by NXP. 

EdgeLock — is a trademark of NXP B.V. 

elQ — is a trademark of NXP B.V. 

I2C-bus — logo is a trademark of NXP B.V. 

NXP SECURE CONNECTIONS FOR A SMARTER WORLD — is a trademark of NXP B.V. 

SafeAssure — is a trademark of NXP B.V. 

SafeAssure — logo is a trademark of NXP B.V. 

SuperFlash This product uses SuperFlash<sup>®</sup> technology. SuperFlash<sup>®</sup> is a registered trademark of Silicon Storage Technology, Inc. 

Synopsys & Designware — are registered trademarks of Synopsys, Inc. 

Synopsys — Portions Copyright<sup>©</sup> 2021 Synopsys, Inc. Used with permission. All rights reserved. 

NXP has a Product Security Incident Response Team (PSIRT) (reachable at PSIRT@nxp.com) that manages the investigation, reporting, and solution release to security vulnerabilities of NXP products. 

Suitability for use in automotive applications — This NXP product has been qualified for use in automotive applications. It has been developed in accordance with ISO 26262 and has been ASIL classified. If this product is used by customer in the development of, or for incorporation into, products or services (a) used in safety critical applications or (b) in which failure could lead to death, personal injury, or severe physical or environmental damage (such products and services hereinafter referred to as “Critical Applications”), then customer makes the ultimate design decisions regarding its products and is solely responsible for compliance with all legal, regulatory, safety, and security related requirements concerning its products, regardless of any information or support that may be provided by NXP. As such, customer assumes all risk related to use of any products in Critical Applications and NXP and its suppliers shall not be liable for any such use by customer. Accordingly, customer will indemnify and hold NXP harmless from any claims, liabilities, damages and associated costs and expenses (including attorneys’ fees) that NXP may incur related to customer’s incorporation of any product in a Critical Application. 

## Trademarks 

Notice: All referenced brands, product names, service names, and trademarks are the property of their respective owners. 

NXP — wordmark and logo are trademarks of NXP B.V. 

AMBA, Arm, Arm7, Arm7TDMI, Arm9, Arm11, Artisan, big.LITTLE, Cordio, CoreLink, CoreSight, Cortex, DesignStart, DynamIQ, Jazelle, Keil, Mali, Mbed, Mbed Enabled, NEON, POP, RealView, SecurCore, Socrates, Thumb, TrustZone, ULINK, ULINK2, ULINK-ME, ULINK-PLUS, ULINKpro, μVision, Versatile — are trademarks or registered trademarks of Arm Limited (or its subsidiaries) in the US and/or elsewhere. The related technology may be protected by any or all of patents, copyrights, designs and trade secrets. All rights reserved. 

Bluetooth — the Bluetooth wordmark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by NXP Semiconductors is under license. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4639 / 4640 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/B_Release_notes/B.82_TEMPSENSE_module_changes/S32K3XXRM_数据表.pdf-4640-00.png)


Please be aware that important notices concerning this document and the product(s) described herein, have been included in section 'Legal information'. 

© NXP B.V. 2022. All rights reserved. 

For more information, please visit: http://www.nxp.com For sales office addresses, please send an email to: salesaddresses@nxp.com 

Date of release: 04/2022 Document identifier: S32K3XXRM 

