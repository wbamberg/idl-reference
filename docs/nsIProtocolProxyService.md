---
layout: default
---

# nsIProtocolProxyService #
  
nsIProtocolProxyService provides methods to access information about  
various network proxies.  
  

## Methods ##

### asyncResolve(aURI, aFlags, aCallback) ###
  
This method returns via callback a nsIProxyInfo instance that identifies  
a proxy to be used for loading the given URI.  Otherwise, this method returns  
null indicating that a direct connection should be used.  
  
@param aURI  
       The URI to test.  
@param aFlags  
       A bit-wise combination of the RESOLVE_ flags defined above.  Pass  
       0 to specify the default behavior.  Any additional bits that do  
       not correspond to a RESOLVE_ flag are reserved for future use.  
@param aCallback  
       The object to be notified when the result is available.  
  
@return An object that can be used to cancel the asychronous operation.  
        If canceled, the cancelation status (aReason) will be forwarded  
        to the callback's onProxyAvailable method via the aStatus param.  
  
NOTE: If this proxy is unavailable, getFailoverForProxy may be called  
to determine the correct secondary proxy to be used.  
  
NOTE: If the protocol handler for the given URI supports  
nsIProxiedProtocolHandler, then the nsIProxyInfo instance returned from  
resolve may be passed to the newProxiedChannel method to create a  
nsIChannel to the given URI that uses the specified proxy.  
  
NOTE: However, if the nsIProxyInfo type is "http", then it means that  
the given URI should be loaded using the HTTP protocol handler, which  
also supports nsIProxiedProtocolHandler.  
  
@see nsIProxiedProtocolHandler::newProxiedChannel   
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI to test.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       A bit-wise combination of the RESOLVE_ flags defined above.  Pass  
       0 to specify the default behavior.  Any additional bits that do  
       not correspond to a RESOLVE_ flag are reserved for future use.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       The object to be notified when the result is available.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An object that can be used to cancel the asychronous operation.  
        If canceled, the cancelation status (aReason) will be forwarded  
        to the callback's onProxyAvailable method via the aStatus param.  
</td>
</tr>

</table>

### newProxyInfo(aType, aHost, aPort, aFlags, aFailoverTimeout, aFailoverProxy) ###
  
This method may be called to construct a nsIProxyInfo instance from  
the given parameters.  This method may be useful in conjunction with  
nsISocketTransportService::createTransport for creating, for example,  
a SOCKS connection.  
  
@param aType  
       The proxy type.  This is a string value that identifies the proxy  
       type.  Standard values include:  
         "http"    - specifies a HTTP proxy  
         "https"   - specifies HTTP proxying over TLS connection to proxy  
         "socks"   - specifies a SOCKS version 5 proxy  
         "socks4"  - specifies a SOCKS version 4 proxy  
         "direct"  - specifies a direct connection (useful for failover)  
       The type name is case-insensitive.  Other string values may be  
       possible, and new types may be defined by a future version of  
       this interface.  
@param aHost  
       The proxy hostname or IP address.  
@param aPort  
       The proxy port.  
@param aFlags  
       Flags associated with this connection.  See nsIProxyInfo.idl  
       for currently defined flags.  
@param aFailoverTimeout  
       Specifies the length of time (in seconds) to ignore this proxy if  
       this proxy fails.  Pass UINT32_MAX to specify the default  
       timeout value, causing nsIProxyInfo::failoverTimeout to be  
       assigned the default value.  
@param aFailoverProxy  
       Specifies the next proxy to try if this proxy fails.  This  
       parameter may be null.  
  

#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>       The proxy type.  This is a string value that identifies the proxy  
       type.  Standard values include:  
         "http"    - specifies a HTTP proxy  
         "https"   - specifies HTTP proxying over TLS connection to proxy  
         "socks"   - specifies a SOCKS version 5 proxy  
         "socks4"  - specifies a SOCKS version 4 proxy  
         "direct"  - specifies a direct connection (useful for failover)  
       The type name is case-insensitive.  Other string values may be  
       possible, and new types may be defined by a future version of  
       this interface.  
</td>
</tr>

<tr>
<td>aHost</td>
<td>       The proxy hostname or IP address.  
</td>
</tr>

<tr>
<td>aPort</td>
<td>       The proxy port.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       Flags associated with this connection.  See nsIProxyInfo.idl  
       for currently defined flags.  
</td>
</tr>

<tr>
<td>aFailoverTimeout</td>
<td>       Specifies the length of time (in seconds) to ignore this proxy if  
       this proxy fails.  Pass UINT32_MAX to specify the default  
       timeout value, causing nsIProxyInfo::failoverTimeout to be  
       assigned the default value.  
</td>
</tr>

<tr>
<td>aFailoverProxy</td>
<td>       Specifies the next proxy to try if this proxy fails.  This  
       parameter may be null.  
</td>
</tr>

</table>

### getFailoverForProxy(aProxyInfo, aURI, aReason) ###
  
If the proxy identified by aProxyInfo is unavailable for some reason,  
this method may be called to access an alternate proxy that may be used  
instead.  As a side-effect, this method may affect future result values  
from resolve/asyncResolve as well as from getFailoverForProxy.  
  
@param aProxyInfo  
       The proxy that was unavailable.  
@param aURI  
       The URI that was originally passed to resolve/asyncResolve.  
@param aReason  
       The error code corresponding to the proxy failure.  This value  
       may be used to tune the delay before this proxy is used again.  
  
@throw NS_ERROR_NOT_AVAILABLE if there is no alternate proxy available.  
  

#### Parameters ####

<table>

<tr>
<td>aProxyInfo</td>
<td>       The proxy that was unavailable.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The URI that was originally passed to resolve/asyncResolve.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>       The error code corresponding to the proxy failure.  This value  
       may be used to tune the delay before this proxy is used again.  
</td>
</tr>

</table>

### registerFilter(aFilter, aPosition) ###
  
This method may be used to register a proxy filter instance.  Each proxy  
filter is registered with an associated position that determines the  
order in which the filters are applied (starting from position 0).  When  
resolve/asyncResolve is called, it generates a list of proxies for the  
given URI, and then it applies the proxy filters.  The filters have the  
opportunity to modify the list of proxies.  
  
If two filters register for the same position, then the filters will be  
visited in the order in which they were registered.  
  
If the filter is already registered, then its position will be updated.  
  
After filters have been run, any disabled or disallowed proxies will be  
removed from the list.  A proxy is disabled if it had previously failed-  
over to another proxy (see getFailoverForProxy).  A proxy is disallowed,  
for example, if it is a HTTP proxy and the nsIProtocolHandler for the  
queried URI does not permit proxying via HTTP.  
  
If a nsIProtocolHandler disallows all proxying, then filters will never  
have a chance to intercept proxy requests for such URLs.  
  
@param aFilter  
       The nsIProtocolProxyFilter instance to be registered.  
@param aPosition  
       The position of the filter.  
  
NOTE: It is possible to construct filters that compete with one another  
in undesirable ways.  This API does not attempt to protect against such  
problems.  It is recommended that any extensions that choose to call  
this method make their position value configurable at runtime (perhaps  
via the preferences service).  
  

#### Parameters ####

<table>

<tr>
<td>aFilter</td>
<td>       The nsIProtocolProxyFilter instance to be registered.  
</td>
</tr>

<tr>
<td>aPosition</td>
<td>       The position of the filter.  
</td>
</tr>

</table>

### unregisterFilter(aFilter) ###
  
This method may be used to unregister a proxy filter instance.  All  
filters will be automatically unregistered at XPCOM shutdown.  
  
@param aFilter  
       The nsIProtocolProxyFilter instance to be unregistered.  
  

#### Parameters ####

<table>

<tr>
<td>aFilter</td>
<td>       The nsIProtocolProxyFilter instance to be unregistered.  
</td>
</tr>

</table>

## Attributes ##

### proxyConfigType ###
  
This attribute specifies the current type of proxy configuration.  
  

## Constants ##

### RESOLVE_PREFER_SOCKS_PROXY ###
 Flag 1 << 0 is unused **/  
  
When the proxy configuration is manual this flag may be passed to the  
resolve and asyncResolve methods to request to prefer the SOCKS proxy  
to HTTP ones.  
  

### RESOLVE_IGNORE_URI_SCHEME ###
  
When the proxy configuration is manual this flag may be passed to the  
resolve and asyncResolve methods to request to not analyze the uri's  
scheme specific proxy. When this flag is set the main HTTP proxy is the  
preferred one.  
  
NOTE: if RESOLVE_PREFER_SOCKS_PROXY is set then the SOCKS proxy is  
      the preferred one.  
  
NOTE: if RESOLVE_PREFER_HTTPS_PROXY is set then the HTTPS proxy  
      is the preferred one.  
  

### RESOLVE_PREFER_HTTPS_PROXY ###
  
When the proxy configuration is manual this flag may be passed to the  
resolve and asyncResolve methods to request to prefer the HTTPS proxy  
to the others HTTP ones.  
  
NOTE: RESOLVE_PREFER_SOCKS_PROXY takes precedence over this flag.  
  
NOTE: This flag implies RESOLVE_IGNORE_URI_SCHEME.  
  

### RESOLVE_ALWAYS_TUNNEL ###
  
When the proxy configuration is manual this flag may be passed to the  
resolve and asyncResolve methods to that all methods will be tunneled via  
CONNECT through the http proxy.  
  

### PROXYCONFIG_DIRECT ###
  
These values correspond to the possible integer values for the  
network.proxy.type preference.  
  

### PROXYCONFIG_MANUAL ###

### PROXYCONFIG_PAC ###

### PROXYCONFIG_WPAD ###

### PROXYCONFIG_SYSTEM ###
