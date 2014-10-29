---
layout: default
---

# nsISSLSocketControl #

## Methods ##

### proxyStartSSL ###

### StartTLS ###

### setNPNList ###

### joinConnection ###

### isAcceptableForHost ###

## Attributes ##

### notificationCallbacks ###

### negotiatedNPN ###

### KEAUsed ###

### KEAExpected ###

### KEAKeyBits ###

### providerFlags ###

### SSLVersionUsed ###

### SSLVersionOffered ###

### MACAlgorithmUsed ###

### clientCert ###

If set before the server requests a client cert (assuming it does so at
all), then this cert will be presented to the server, instead of asking
the user or searching the set of rememebered user cert decisions.


### authenticationName ###

If you wish to verify the host certificate using a different name than
was used for the tcp connection, but without using proxy semantics, you
can set authenticationName and authenticationPort


### authenticationPort ###

### bypassAuthentication ###

set bypassAuthentication to true if the server certificate checks should
not be enforced. This is to enable non-secure transport over TLS.


### failedVerification ###

## Constants ##

### KEY_EXCHANGE_UNKNOWN ###

### SSL_VERSION_3 ###

### TLS_VERSION_1 ###

### TLS_VERSION_1_1 ###

### TLS_VERSION_1_2 ###

### SSL_VERSION_UNKNOWN ###

### SSL_MAC_UNKNOWN ###

### SSL_MAC_NULL ###

### SSL_MAC_MD5 ###

### SSL_MAC_SHA ###

### SSL_HMAC_MD5 ###

### SSL_HMAC_SHA ###

### SSL_HMAC_SHA256 ###

### SSL_MAC_AEAD ###
