---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIProxiedProtocolHandler.idl">Source file</a>
</div>

# nsIProxiedProtocolHandler #

## Methods ##

### newProxiedChannel2(uri, proxyInfo, proxyResolveFlags, proxyURI, aLoadInfo) ###
<code> Create a new channel with the given proxyInfo  
  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>the channel uri  
</td>
</tr>

<tr>
<td>proxyInfo</td>
<td>any proxy information that has already been determined,  
       or null if channel should later determine the proxy on its own using  
       proxyResolveFlags/proxyURI  
</td>
</tr>

<tr>
<td>proxyResolveFlags</td>
<td>used if the proxy is later determined  
       from nsIProtocolProxyService::asyncResolve  
</td>
</tr>

<tr>
<td>proxyURI</td>
<td>used if the proxy is later determined from  
       nsIProtocolProxyService::asyncResolve with this as the proxyURI name.  
       Generally this is the same as uri (or null which has the same  
       effect), except in the case of websockets which wants to bootstrap  
       to an http:// channel but make its proxy determination based on  
       a ws:// uri.  
</td>
</tr>

</table>

### newProxiedChannel(uri, proxyInfo, proxyResolveFlags, proxyURI) ###
<code> Create a new channel with the given proxyInfo  
  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>the channel uri  
</td>
</tr>

<tr>
<td>proxyInfo</td>
<td>any proxy information that has already been determined,  
       or null if channel should later determine the proxy on its own using  
       proxyResolveFlags/proxyURI  
</td>
</tr>

<tr>
<td>proxyResolveFlags</td>
<td>used if the proxy is later determined  
       from nsIProtocolProxyService::asyncResolve  
</td>
</tr>

<tr>
<td>proxyURI</td>
<td>used if the proxy is later determined from  
       nsIProtocolProxyService::asyncResolve with this as the proxyURI name.  
       Generally this is the same as uri (or null which has the same  
       effect), except in the case of websockets which wants to bootstrap  
       to an http:// channel but make its proxy determination based on  
       a ws:// uri.  
</td>
</tr>

</table>
