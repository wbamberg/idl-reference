---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIProtocolProxyFilter.idl">Source file</a>
</div>

# nsIProtocolProxyFilter #
  
This interface is used to apply filters to the proxies selected for a given  
URI.  Use nsIProtocolProxyService::registerFilter to hook up instances of  
this interface.  
  

## Methods ##

### applyFilter(aProxyService, aURI, aProxy) ###
  
This method is called to apply proxy filter rules for the given URI  
and proxy object (or list of proxy objects).  
  
  
  

#### Parameters ####

<table>

<tr>
<td>aProxyService</td>
<td>       A reference to the Protocol Proxy Service.  This is passed so that  
       implementations may easily access methods such as newProxyInfo.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The URI for which these proxy settings apply.  
</td>
</tr>

<tr>
<td>aProxy</td>
<td>       The proxy (or list of proxies) that would be used by default for  
       the given URI.  This may be null.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The proxy (or list of proxies) that should be used in place of  
        aProxy.  This can be just be aProxy if the filter chooses not to  
        modify the proxy.  It can also be null to indicate that a direct  
        connection should be used.  Use aProxyService.newProxyInfo to  
        construct nsIProxyInfo objects.  
</td>
</tr>

</table>
