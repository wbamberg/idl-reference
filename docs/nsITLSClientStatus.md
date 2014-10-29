---
layout: default
---

# nsITLSClientStatus #

Security summary for a given TLS client connection being handled by a
|nsITLSServerSocket| server.

This is accessible through the security info object on the transport, which
will be an instance of |nsITLSServerConnectionInfo| (see below).

The values of these attributes are available once the |onHandshakeDone|
method of the security observer has been called (see
|nsITLSServerSecurityObserver| below).


## peerCert ##

peerCert

The client's certificate, if one was requested via |requestCertificate|
above and supplied by the client.


## SSL_VERSION_3 ##

Values for tlsVersionUsed, as defined by TLS


## TLS_VERSION_1 ##

## TLS_VERSION_1_1 ##

## TLS_VERSION_1_2 ##

## TLS_VERSION_UNKNOWN ##

## tlsVersionUsed ##

tlsVersionUsed

The version of TLS used by the connection.  See values above.


## cipherName ##

cipherName

Name of the cipher suite used, such as
"TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256".
See security/nss/lib/ssl/sslinfo.c for the possible values.


## keyLength ##

keyLength

The "effective" key size of the symmetric key in bits.


## macLength ##

macLength

The size of the MAC in bits.

