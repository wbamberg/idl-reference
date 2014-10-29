---
layout: default
---

# nsICdmaCellInfo #

## networkId ##

Network Id, 0..65535, INT_MAX if unknown.


## systemId ##

CDMA System Id, 0..32767, INT_MAX if unknown.


## baseStationId ##

Base Station Id, 0..65535, INT_MAX if unknown.


## longitude ##

Longitude is a decimal number as specified in 3GPP2 C.S0005-A v6.0.
It is represented in units of 0.25 seconds and ranges from -2592000 to
2592000, INT_MAX if unknown.


## latitude ##

Latitude is a decimal number as specified in 3GPP2 C.S0005-A v6.0.
It is represented in units of 0.25 seconds and ranges from -1296000 to
1296000, INT_MAX if unknown.


## cdmaDbm ##

Valid values are positive integers, INT_MAX if unknown. This value is the
actual RSSI value multiplied by -1.


## cdmaEcio ##

Valid values are positive integers, INT_MAX if unknown. This value is the
actual Ec/Io multiplied by -10. -1 if unknown.


## evdoDbm ##

Valid values are positive integers, INT_MAX if unknown. This value is the
actual Evdo RSSI value multiplied by -1.


## evdoEcio ##

Valid values are positive integers, INT_MAX if unknown. This value is the
actual Evdo Ec/Io multiplied by -10.


## evdoSnr ##

Valid values are 0-8, INT_MAX if unknown. 8 is the highest signal to noise
ratio.

