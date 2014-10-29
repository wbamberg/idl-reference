---
layout: default
---

# nsILteCellInfo #

## Attributes ##

### mcc ###

3-digit Mobile Country Code, 0..999, INT_MAX if unknown.


### mnc ###

2 or 3-digit Mobile Network Code, 0..999, INT_MAX if unknown.


### cid ###

28-bit Cell Identity, 0..268435455, INT_MAX if unknown.


### pcid ###

Physical cell id, 0..503, INT_MAX if unknown.


### tac ###

16-bit tracking area code, 0..65535, INT_MAX if unknown.


### signalStrength ###

Valid values are 0-31 as defined in TS 27.007 8.5, 99 if unknown.


### rsrp ###

The current Reference Signal Receive Power in dBm multipled by -1.
Range: 44 to 140 dBm, INT_MAX if unknown.


### rsrq ###

The current Reference Signal Receive Quality in dB multiplied by -1.
Range: 3 to 20 dB, INT_MAX if unknown.


### rssnr ###

The current reference signal signal-to-noise ratio in 0.1 dB units.
Range: -200 to +300 (-200 = -20.0 dB, +300 = 30dB), INT_MAX if unknown.


### cqi ###

The current Channel Quality Indicator. Range: 0 to 15, INT_MAX if unknown.


### timingAdvance ###

Timing advance in micro seconds for a one way trip from cell to device.
Approximate distance can be calculated using 300m/us * timingAdvance.
Range: 0 to 0x7FFFFFFE, INT_MAX if unknown.

