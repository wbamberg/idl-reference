---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsITLSServerSocket.idl">Source file</a>
</div>

# nsITLSClientStatus #
<pre>  
Security summary for a given TLS client connection being handled by a  
|nsITLSServerSocket| server.  
  
This is accessible through the security info object on the transport, which  
will be an instance of |nsITLSServerConnectionInfo| (see below).  
  
The values of these attributes are available once the |onHandshakeDone|  
method of the security observer has been called (see  
|nsITLSServerSecurityObserver| below).  
  
</pre>
## Attributes ##

### peerCert ###
<pre>  
peerCert  
  
The client's certificate, if one was requested via |requestCertificate|  
above and supplied by the client.  
  
</pre>
### tlsVersionUsed ###
<pre>  
tlsVersionUsed  
  
The version of TLS used by the connection.  See values above.  
  
</pre>
### cipherName ###
<pre>  
cipherName  
  
Name of the cipher suite used, such as  
"TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256".  
See security/nss/lib/ssl/sslinfo.c for the possible values.  
  
</pre>
### keyLength ###
<pre>  
keyLength  
  
The "effective" key size of the symmetric key in bits.  
  
</pre>
### macLength ###
<pre>  
macLength  
  
The size of the MAC in bits.  
  
</pre>
## Constants ##

### SSL_VERSION_3 ###
<pre>  
Values for tlsVersionUsed, as defined by TLS  
  
</pre>
### TLS_VERSION_1 ###

### TLS_VERSION_1_1 ###

### TLS_VERSION_1_2 ###

### TLS_VERSION_UNKNOWN ###
