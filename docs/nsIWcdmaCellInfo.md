---
layout: default
---

# nsIWcdmaCellInfo #

## Attributes ##

### mcc ###

2 or 3-digit Mobile Network Code, 0..999, INT_MAX if unknown.


### mnc ###

2 or 3-digit Mobile Network Code, 0..999, INT_MAX if unknown.


### lac ###

16-bit Location Area Code, 0..65535, INT_MAX if unknown.


### cid ###

28-bit UMTS Cell Identity described in TS 25.331, 0..268435455,
INT_MAX if unknown.


### psc ###

9-bit UMTS Primary Scrambling Code described in TS 25.331, 0..511,
INT_MAX if unknown.


### signalStrength ###

Valid values are 0-31 as defined in TS 27.007 8.5, 99 if unknown.


### bitErrorRate ###

Bit error rate 0-7 as defined in TS 27.007 8.5, 99 if unknown.

