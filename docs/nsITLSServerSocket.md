---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsITLSServerSocket.idl">Source file</a>
</div>
# nsITLSServerSocket #

## Methods ##

### setSessionCache(aSessionCache) ###
  
setSessionCache  
  
Whether the server should use a session cache.  Defaults to true.  This  
should be set before calling |asyncListen| if you wish to change the  
default.  
  

### setSessionTickets(aSessionTickets) ###
  
setSessionTickets  
  
Whether the server should support session tickets.  Defaults to true.  This  
should be set before calling |asyncListen| if you wish to change the  
default.  
  

### setRequestClientCertificate(aRequestClientCert) ###
  
setRequestClientCertificate  
  
Whether the server should request and/or require a client auth certificate  
from the client.  Defaults to REQUEST_NEVER.  See the possible options  
above.  This should be set before calling |asyncListen| if you wish to  
change the default.  
  

## Attributes ##

### serverCert ###
  
serverCert  
  
The server's certificate that is presented to the client during the TLS  
handshake.  This is required to be set before calling |asyncListen|.  
  

## Constants ##

### REQUEST_NEVER ###
  
Values for setRequestClientCertificate  
  

### REQUEST_FIRST_HANDSHAKE ###

### REQUEST_ALWAYS ###

### REQUIRE_FIRST_HANDSHAKE ###

### REQUIRE_ALWAYS ###
