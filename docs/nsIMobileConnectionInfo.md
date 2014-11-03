---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsIMobileConnectionInfo.idl">Source file</a>
</div>

# nsIMobileConnectionInfo #

## Attributes ##

### state ###
<pre>  
State of the connection.  
  
Possible values: 'notSearching', 'searching', 'denied', 'registered' or  
                 null (unknown).  
  
</pre>
### connected ###
<pre>  
Indicates whether the connection is ready.  
  
Note: The meaning of "connection ready" for data and voice are different.  
      - Data: the "default" data connection is established or not.  
      - Voice: voice is registered to network or not.  
  
</pre>
### emergencyCallsOnly ###
<pre>  
Indicates whether only emergency calls are possible.  
  
This flag is only relevant to voice connections and when 'connected' is  
false.  
  
</pre>
### roaming ###
<pre>  
Indicates whether the connection is going through a foreign operator  
(roaming) or not.  
  
</pre>
### network ###
<pre>  
Network operator information.  
  
</pre>
### type ###
<pre>  
Type of connection.  
  
Possible values: 'gsm', 'gprs', 'edge', 'umts', 'hsdpa', 'hsupa', 'hspa',  
                 'hspa+', 'is95a', 'is95b', '1xrtt', 'evdo0', 'evdoa',  
                 'evdob', 'ehrpd', 'lte' or null (unknown).  
  
</pre>
### signalStrength ###
<pre>  
Signal strength in dBm, or null if no service is available.  
  
</pre>
### relSignalStrength ###
<pre>  
Signal strength, represented linearly as a number between 0 (weakest  
signal) and 100 (full signal).  
  
</pre>
### cell ###
<pre>  
Cell location information.  
  
</pre>