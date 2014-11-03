---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsITLSServerSocket.idl">Source file</a>
</div>

# nsITLSServerSocket #

## Methods ##

### setSessionCache(aSessionCache) ###
<pre>  
setSessionCache  
  
Whether the server should use a session cache.  Defaults to true.  This  
should be set before calling |asyncListen| if you wish to change the  
default.  
  
</pre>
### setSessionTickets(aSessionTickets) ###
<pre>  
setSessionTickets  
  
Whether the server should support session tickets.  Defaults to true.  This  
should be set before calling |asyncListen| if you wish to change the  
default.  
  
</pre>
### setRequestClientCertificate(aRequestClientCert) ###
<pre>  
setRequestClientCertificate  
  
Whether the server should request and/or require a client auth certificate  
from the client.  Defaults to REQUEST_NEVER.  See the possible options  
above.  This should be set before calling |asyncListen| if you wish to  
change the default.  
  
</pre>
## Attributes ##

### serverCert ###
<pre>  
serverCert  
  
The server's certificate that is presented to the client during the TLS  
handshake.  This is required to be set before calling |asyncListen|.  
  
</pre>
## Constants ##

### REQUEST_NEVER ###
<pre>  
Values for setRequestClientCertificate  
  
</pre>
### REQUEST_FIRST_HANDSHAKE ###

### REQUEST_ALWAYS ###

### REQUIRE_FIRST_HANDSHAKE ###

### REQUIRE_ALWAYS ###
