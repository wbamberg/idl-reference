---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIProxyInfo.idl">Source file</a>
</div>

# nsIProxyInfo #
  
This interface identifies a proxy server.  
  

## Attributes ##

### host ###
  
This attribute specifies the hostname of the proxy server.  
  

### port ###
  
This attribute specifies the port number of the proxy server.  
  

### type ###
  
This attribute specifies the type of the proxy server as an ASCII string.  
  
Some special values for this attribute include (but are not limited to)  
the following:  
  "http"     HTTP proxy (or SSL CONNECT for HTTPS)  
  "https"    HTTP proxying over TLS connection to proxy  
  "socks"    SOCKS v5 proxy  
  "socks4"   SOCKS v4 proxy  
  "direct"   no proxy  
  "unknown"  unknown proxy (see nsIProtocolProxyService::resolve)  
  
A future version of this interface may define additional types.  
  

### flags ###
  
This attribute specifies flags that modify the proxy type.  The value of  
this attribute is the bit-wise combination of the Proxy Flags defined  
below.  Any undefined bits are reserved for future use.  
  

### resolveFlags ###
  
This attribute specifies flags that were used by nsIProxyProtocolService when  
creating this ProxyInfo element.   
  

### failoverTimeout ###
  
This attribute specifies the failover timeout in seconds for this proxy.  
If a nsIProxyInfo is reported as failed via nsIProtocolProxyService::  
getFailoverForProxy, then the failed proxy will not be used again for this  
many seconds.  
  

### failoverProxy ###
  
This attribute specifies the proxy to failover to when this proxy fails.  
  

## Constants ##

### TRANSPARENT_PROXY_RESOLVES_HOST ###
************************************************************************  
The following "Proxy Flags" may be bit-wise combined to construct the  
flags attribute defined on this interface.  All unspecified bits are  
reserved for future use.  
  
  
This flag is set if the proxy is to perform name resolution itself.  If  
this is the case, the hostname is used in some fashion, and we shouldn't  
do any form of DNS lookup ourselves.  
  
