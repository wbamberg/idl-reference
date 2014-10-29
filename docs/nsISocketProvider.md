---
layout: default
---

# nsISocketProvider #

nsISocketProvider


## newSocket ##

newSocket

@param aFamily
       The address family for this socket (PR_AF_INET or PR_AF_INET6).
@param aHost
       The hostname for this connection.
@param aPort
       The port for this connection.
@param aProxyHost
       If non-null, the proxy hostname for this connection.
@param aProxyPort
       The proxy port for this connection.
@param aFlags
       Control flags that govern this connection (see below.)
@param aFileDesc
       The resulting PRFileDesc.
@param aSecurityInfo
       Any security info that should be associated with aFileDesc.  This
       object typically implements nsITransportSecurityInfo.


## addToSocket ##

addToSocket

This function is called to allow the socket provider to layer a
PRFileDesc on top of another PRFileDesc.  For example, SSL via a SOCKS
proxy.

Parameters are the same as newSocket with the exception of aFileDesc,
which is an in-param instead.


## PROXY_RESOLVES_HOST ##

PROXY_RESOLVES_HOST

This flag is set if the proxy is to perform hostname resolution instead
of the client.  When set, the hostname parameter passed when in this
interface will be used instead of the address structure passed for a
later connect et al. request.


## ANONYMOUS_CONNECT ##

When setting this flag, the socket will not apply any
credentials when establishing a connection. For example,
an SSL connection would not send any client-certificates
if this flag is set.


## NO_PERMANENT_STORAGE ##

If set, indicates that the connection was initiated from a source
defined as being private in the sense of Private Browsing. Generally,
there should be no state shared between connections that are private
and those that are not; it is OK for multiple private connections
to share state with each other, and it is OK for multiple non-private
connections to share state with each other.

