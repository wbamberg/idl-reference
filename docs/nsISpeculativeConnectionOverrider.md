---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISpeculativeConnect.idl">Source file</a>
</div>

# nsISpeculativeConnectionOverrider #
  
This is used to override the default values for various values (documented  
inline) to determine whether or not to actually make a speculative  
connection.  
  

## Attributes ##

### parallelSpeculativeConnectLimit ###
  
Used to determine the maximum number of unused speculative connections  
we will have open for a host at any one time  
  

### ignorePossibleSpdyConnections ###
  
Used to loosen the restrictions nsHttpConnectionMgr::RestrictConnections  
to allow more speculative connections when we're unsure if a host will  
connect via SPDY or not.  
  

### ignoreIdle ###
  
Used to determine if we will ignore the existence of any currently idle  
connections when we decide whether or not to make a speculative  
connection.  
  

### isFromPredictor ###

### allow1918 ###
  
by default speculative connections are not made to RFC 1918 addresses  
  
