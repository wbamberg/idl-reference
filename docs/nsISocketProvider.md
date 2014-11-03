---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/socket/nsISocketProvider.idl">Source file</a>
</div>

# nsISocketProvider #
<pre>  
nsISocketProvider  
  
</pre>
## Methods ##

### newSocket(aFamily, aHost, aPort, aProxyHost, aProxyPort, aFlags, aFileDesc, aSecurityInfo) ###
<pre>  
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
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aFamily</td>
<td>       The address family for this socket (PR_AF_INET or PR_AF_INET6).  
</td>
</tr>

<tr>
<td>aHost</td>
<td>       The hostname for this connection.  
</td>
</tr>

<tr>
<td>aPort</td>
<td>       The port for this connection.  
</td>
</tr>

<tr>
<td>aProxyHost</td>
<td>       If non-null, the proxy hostname for this connection.  
</td>
</tr>

<tr>
<td>aProxyPort</td>
<td>       The proxy port for this connection.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       Control flags that govern this connection (see below.)  
</td>
</tr>

<tr>
<td>aFileDesc</td>
<td>       The resulting PRFileDesc.  
</td>
</tr>

<tr>
<td>aSecurityInfo</td>
<td>       Any security info that should be associated with aFileDesc.  This  
       object typically implements nsITransportSecurityInfo.  
</td>
</tr>

</table>

### addToSocket(aFamily, aHost, aPort, aProxyHost, aProxyPort, aFlags, aFileDesc, aSecurityInfo) ###
<pre>  
addToSocket  
  
This function is called to allow the socket provider to layer a  
PRFileDesc on top of another PRFileDesc.  For example, SSL via a SOCKS  
proxy.  
  
Parameters are the same as newSocket with the exception of aFileDesc,  
which is an in-param instead.  
  
</pre>
## Constants ##

### PROXY_RESOLVES_HOST ###
<pre>  
PROXY_RESOLVES_HOST  
  
This flag is set if the proxy is to perform hostname resolution instead  
of the client.  When set, the hostname parameter passed when in this  
interface will be used instead of the address structure passed for a  
later connect et al. request.  
  
</pre>
### ANONYMOUS_CONNECT ###
<pre>  
When setting this flag, the socket will not apply any  
credentials when establishing a connection. For example,  
an SSL connection would not send any client-certificates  
if this flag is set.  
  
</pre>
### NO_PERMANENT_STORAGE ###
<pre>  
If set, indicates that the connection was initiated from a source  
defined as being private in the sense of Private Browsing. Generally,  
there should be no state shared between connections that are private  
and those that are not; it is OK for multiple private connections  
to share state with each other, and it is OK for multiple non-private  
connections to share state with each other.  
  
</pre>