---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIUDPSocketFilter.idl">Source file</a>
</div>

# nsIUDPSocketFilter #
<pre>  
Filters are created and run on the parent, and filter all UDP packets, both  
ingoing and outgoing. The child must specify the name of a recognized filter  
in order to create a UDP socket.  
  
</pre>
## Methods ##

### filterPacket(remote_addr, data, len, direction) ###

## Constants ##

### SF_INCOMING ###

### SF_OUTGOING ###
