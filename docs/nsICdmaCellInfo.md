---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsICellInfo.idl">Source file</a>
</div>

# nsICdmaCellInfo #

## Attributes ##

### networkId ###
<pre>  
Network Id, 0..65535, INT_MAX if unknown.  
  
</pre>
### systemId ###
<pre>  
CDMA System Id, 0..32767, INT_MAX if unknown.  
  
</pre>
### baseStationId ###
<pre>  
Base Station Id, 0..65535, INT_MAX if unknown.  
  
</pre>
### longitude ###
<pre>  
Longitude is a decimal number as specified in 3GPP2 C.S0005-A v6.0.  
It is represented in units of 0.25 seconds and ranges from -2592000 to  
2592000, INT_MAX if unknown.  
  
</pre>
### latitude ###
<pre>  
Latitude is a decimal number as specified in 3GPP2 C.S0005-A v6.0.  
It is represented in units of 0.25 seconds and ranges from -1296000 to  
1296000, INT_MAX if unknown.  
  
</pre>
### cdmaDbm ###
<pre>  
Valid values are positive integers, INT_MAX if unknown. This value is the  
actual RSSI value multiplied by -1.  
  
</pre>
### cdmaEcio ###
<pre>  
Valid values are positive integers, INT_MAX if unknown. This value is the  
actual Ec/Io multiplied by -10. -1 if unknown.  
  
</pre>
### evdoDbm ###
<pre>  
Valid values are positive integers, INT_MAX if unknown. This value is the  
actual Evdo RSSI value multiplied by -1.  
  
</pre>
### evdoEcio ###
<pre>  
Valid values are positive integers, INT_MAX if unknown. This value is the  
actual Evdo Ec/Io multiplied by -10.  
  
</pre>
### evdoSnr ###
<pre>  
Valid values are 0-8, INT_MAX if unknown. 8 is the highest signal to noise  
ratio.  
  
</pre>