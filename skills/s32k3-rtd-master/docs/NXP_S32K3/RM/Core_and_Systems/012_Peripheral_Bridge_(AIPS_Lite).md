NXP Semiconductors 

# Chapter 12 Peripheral Bridge (AIPS_Lite) 

## 12.1 Chip-specific AIPS_Lite information 

### 12.1.1 AIPS_Lite instances 

The following table summarizes AIPS_Lite instances on S32K3xx product series to support simultaneous data transfers to different peripherals. See the memory map file attached to this document to find information related to these peripherals that are associated with AIPS_Lite instances. 

Table 42. AIPS_Lite instances 

|Instance|K358|K344|K324|K314|K342|K322|K312|K311|
|---|---|---|---|---|---|---|---|---|
|AIPS_0|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|AIPS_1|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|AIPS_2|Yes|Yes|Yes|Yes|Yes|Yes|No|No|



## 12.2 Introduction 

AIPS_Lite converts the crossbar switch interface to an interface that can access most of the slave peripherals on this chip. 

This peripheral bridge occupies 64 MB of the address space, which is divided into peripheral slots of 16 KB each. All the peripherals may not be used. See the memory map chapter for details on slot assignments. The bridge includes separate clock enable inputs for each of the slots to accommodate slower peripherals. 

### 12.2.1 Features 

Following are the key features of the peripheral bridge: 

- Supports peripheral slots with 8-, 16-, and 32-bit datapath width 

- Supports a pair of 32-bit transactions for selected 64-bit memory accesses 

### 12.2.2 General operation 

The slave devices connected to the peripheral bridge are modules that contain a programming model of control and status registers. The system masters read and write these registers through the peripheral bridge. 

The register maps of the peripherals are located on 16 KB boundaries. Each peripheral is allocated one or more 16-KB block(s) of the memory map. 

## 12.3 Functional description 

The peripheral bridge functions as a bus protocol translator between the crossbar switch and the slave peripheral bus. Support is provided for generating a pair of 32-bit slave accesses when performing certain 64-bit peripheral accesses. 

The peripheral bridge manages all transactions for the attached slave devices and generates select signals for modules on the peripheral bus by decoding accesses within the attached address space. 

### 12.3.1 Access support 

All combinations of access size and peripheral data port width are supported. An access that is larger than the target peripheral's data width is decomposed to multiple, smaller accesses. Bus decomposition is terminated by a transfer error caused by an access to an empty register area. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

392 / 4640 

NXP Semiconductors 

Peripheral Bridge (AIPS_Lite) 

## 12.4 Memory map and register definition 

The AIPS module(s) on this chip do(es) not contain any user-programmable registers. 

## 12.5 Glossary 

ID Master port number 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

393 / 4640 

