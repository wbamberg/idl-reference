---
layout: default
---

# nsIProxiedProtocolHandler #

## newProxiedChannel2 ##
 Create a new channel with the given proxyInfo

@param uri the channel uri
@param proxyInfo any proxy information that has already been determined,
       or null if channel should later determine the proxy on its own using
       proxyResolveFlags/proxyURI
@param proxyResolveFlags used if the proxy is later determined
       from nsIProtocolProxyService::asyncResolve
@param proxyURI used if the proxy is later determined from
       nsIProtocolProxyService::asyncResolve with this as the proxyURI name.
       Generally this is the same as uri (or null which has the same
       effect), except in the case of websockets which wants to bootstrap
       to an http:// channel but make its proxy determination based on
       a ws:// uri.


## newProxiedChannel ##
 Create a new channel with the given proxyInfo

@param uri the channel uri
@param proxyInfo any proxy information that has already been determined,
       or null if channel should later determine the proxy on its own using
       proxyResolveFlags/proxyURI
@param proxyResolveFlags used if the proxy is later determined
       from nsIProtocolProxyService::asyncResolve
@param proxyURI used if the proxy is later determined from
       nsIProtocolProxyService::asyncResolve with this as the proxyURI name.
       Generally this is the same as uri (or null which has the same
       effect), except in the case of websockets which wants to bootstrap
       to an http:// channel but make its proxy determination based on
       a ws:// uri.

