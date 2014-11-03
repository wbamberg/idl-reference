---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/socket/nsITransportSecurityInfo.idl">Source file</a>
</div>

# nsITransportSecurityInfo #

## Attributes ##

### securityState ###

### errorMessage ###

### failedCertChain ###
<pre>  
If certificate verification failed, this will be the peer certificate  
chain provided in the handshake, so it can be used for error reporting.  
If verification succeeded, this will be null.  
  
</pre>