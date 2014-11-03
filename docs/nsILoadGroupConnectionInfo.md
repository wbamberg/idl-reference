---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsILoadGroup.idl">Source file</a>
</div>

# nsILoadGroupConnectionInfo #
<pre>  
Used to maintain state about the connections of a load group and  
how they interact with blocking items like HEAD css/js loads.  
  
</pre>
## Methods ##

### addBlockingTransaction() ###
<pre>  
Increase the number of active blocking transactions associated  
with this load group by one.  
  
</pre>
### removeBlockingTransaction() ###
<pre>  
Decrease the number of active blocking transactions associated  
with this load group by one. The return value is the number of remaining  
blockers.  
  
</pre>
## Attributes ##

### blockingTransactionCount ###
<pre>  
Number of active blocking transactions associated with this load group  
  
</pre>
### spdyPushCache ###
