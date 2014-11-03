---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsITLSServerSocket.idl">Source file</a>
</div>

# nsITLSServerSecurityObserver #

## Methods ##

### onHandshakeDone(aServer, aStatus) ###
<code>  
onHandsakeDone  
  
This method is called once the TLS handshake is completed.  This takes  
place after |onSocketAccepted| has been called, which typically opens the  
streams to keep things moving along. It's important to be aware that the  
handshake has not completed at the point that |onSocketAccepted| is called,  
so no security verification can be done until this method is called.  
  
</code>