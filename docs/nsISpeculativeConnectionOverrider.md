---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISpeculativeConnect.idl">Source file</a>
</div>

# nsISpeculativeConnectionOverrider #
<pre>  
This is used to override the default values for various values (documented  
inline) to determine whether or not to actually make a speculative  
connection.  
  
</pre>
## Attributes ##

### parallelSpeculativeConnectLimit ###
<pre>  
Used to determine the maximum number of unused speculative connections  
we will have open for a host at any one time  
  
</pre>
### ignorePossibleSpdyConnections ###
<pre>  
Used to loosen the restrictions nsHttpConnectionMgr::RestrictConnections  
to allow more speculative connections when we're unsure if a host will  
connect via SPDY or not.  
  
</pre>
### ignoreIdle ###
<pre>  
Used to determine if we will ignore the existence of any currently idle  
connections when we decide whether or not to make a speculative  
connection.  
  
</pre>
### isFromPredictor ###

### allow1918 ###
<pre>  
by default speculative connections are not made to RFC 1918 addresses  
  
</pre>