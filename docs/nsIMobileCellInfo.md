---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsIMobileCellInfo.idl">Source file</a>
</div>

# nsIMobileCellInfo #

## Attributes ##

### gsmLocationAreaCode ###
  
Mobile Location Area Code (LAC) for GSM/WCDMA networks.  
  
Possible ranges from 0x0000 to 0xffff.  
-1 if the LAC is unknown.  
  

### gsmCellId ###
  
Mobile Cell ID for GSM/WCDMA networks.  
  
Possible ranges from 0x00000000 to 0xffffffff.  
-1 if the cell id is unknown.  
  

### cdmaBaseStationId ###
  
Base Station ID for CDMA networks.  
  
Possible ranges from 0 to 65535.  
-1 if the base station id is unknown.  
  

### cdmaBaseStationLatitude ###
  
Base Station Latitude for CDMA networks.  
  
Possible ranges from -1296000 to 1296000.  
-2147483648 if the latitude is unknown.  
  
@see 3GPP2 C.S0005-A v6.0.  
  

### cdmaBaseStationLongitude ###
  
Base Station Longitude for CDMA networks.  
  
Possible ranges from -2592000 to 2592000.  
-2147483648 if the longitude is unknown.  
  
@see 3GPP2 C.S0005-A v6.0.  
  

### cdmaSystemId ###
  
System ID for CDMA networks.  
  
Possible ranges from 0 to 32767.  
-1 if the system id is unknown.  
  

### cdmaNetworkId ###
  
Network ID for CDMA networks.  
  
Possible ranges from 0 to 65535.  
-1 if the network id is unknown.  
  
