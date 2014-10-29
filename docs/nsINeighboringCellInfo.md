---
layout: default
---

# nsINeighboringCellInfo #

## networkType ##

Type of radio technology.

Possible values: 'gsm', 'gprs', 'edge', 'umts', 'hsdpa', 'hsupa', 'hspa',
                 'hspa+' or null (unknown).


## gsmLocationAreaCode ##

Mobile Location Area Code (LAC) for GSM networks.

Possible ranges from 0x0000 to 0xffff.
-1 if the LAC is unknown.


## gsmCellId ##

Mobile Cell ID for GSM networks.

Possible ranges from 0x00000000 to 0xffffffff.
-1 if the cell id is unknown.


## wcdmaPsc ##

Primary Scrambling Code (PSC) for WCDMA networks.

Possible ranges from 0x0000 to 0x01ff.
-1 if the psc is unknown.


## signalStrength ##

For GSM networks, signalStrength is the received rssi, ranging from 0 to 31.
For WCDMA networks, signalStrength is the CPICH Received Signal Code Power,
ranging from -120 to -25.

99 if signalStrength is unknown.

