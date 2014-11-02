---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsILoadGroup.idl">Source file</a>
</div>

# nsILoadGroupConnectionInfo #
  
Used to maintain state about the connections of a load group and  
how they interact with blocking items like HEAD css/js loads.  
  

## Methods ##

### addBlockingTransaction() ###
  
Increase the number of active blocking transactions associated  
with this load group by one.  
  

### removeBlockingTransaction() ###
  
Decrease the number of active blocking transactions associated  
with this load group by one. The return value is the number of remaining  
blockers.  
  

## Attributes ##

### blockingTransactionCount ###
  
Number of active blocking transactions associated with this load group  
  

### spdyPushCache ###
