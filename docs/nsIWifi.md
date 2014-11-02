---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/wifi/nsIWifi.idl">Source file</a>
</div>
# nsIWifi #

## Methods ##

### shutdown() ###
  
Shutdown the wifi system.  
  

### getWifiScanResults(callback) ###
  
Returns the list of currently available networks as well as the list of  
currently configured networks.  
  
On success a callback is notified with the list of networks.  
On failure after 3 scan retry attempts a callback is notified of failure.  
  
