---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsITLSServerSocket.idl">Source file</a>
</div>

# nsITLSServerConnectionInfo #
<pre>  
Connection info for a given TLS client connection being handled by a  
|nsITLSServerSocket| server.  This object is thread-safe.  
  
This is exposed as the security info object on the transport, so it can be  
accessed via |transport.securityInfo|.  
  
This interface is available by the time the |onSocketAttached| is called,  
which is the first time the TLS server consumer is notified of a new client.  
  
</pre>
## Methods ##

### setSecurityObserver(observer) ###
<pre>  
setSecurityObserver  
  
Set the security observer to be notified when the TLS handshake has  
completed.  
  
</pre>
## Attributes ##

### serverSocket ###
<pre>  
serverSocket  
  
The nsITLSServerSocket instance that accepted this client connection.  
  
</pre>
### status ###
<pre>  
status  
  
Security summary for this TLS client connection.  Note that the values of  
this interface are not available until the TLS handshake has completed.  
See |nsITLSClientStatus| above for more details.  
  
</pre>