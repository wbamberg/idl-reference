---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsINeighboringCellInfo.idl">Source file</a>
</div>

# nsINeighboringCellInfo #

## Attributes ##

### networkType ###
<pre>  
Type of radio technology.  
  
Possible values: 'gsm', 'gprs', 'edge', 'umts', 'hsdpa', 'hsupa', 'hspa',  
                 'hspa+' or null (unknown).  
  
</pre>
### gsmLocationAreaCode ###
<pre>  
Mobile Location Area Code (LAC) for GSM networks.  
  
Possible ranges from 0x0000 to 0xffff.  
-1 if the LAC is unknown.  
  
</pre>
### gsmCellId ###
<pre>  
Mobile Cell ID for GSM networks.  
  
Possible ranges from 0x00000000 to 0xffffffff.  
-1 if the cell id is unknown.  
  
</pre>
### wcdmaPsc ###
<pre>  
Primary Scrambling Code (PSC) for WCDMA networks.  
  
Possible ranges from 0x0000 to 0x01ff.  
-1 if the psc is unknown.  
  
</pre>
### signalStrength ###
<pre>  
For GSM networks, signalStrength is the received rssi, ranging from 0 to 31.  
For WCDMA networks, signalStrength is the CPICH Received Signal Code Power,  
ranging from -120 to -25.  
  
99 if signalStrength is unknown.  
  
</pre>