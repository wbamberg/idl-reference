---
layout: default
---

# nsIIOService2 #
  
nsIIOService2 extends nsIIOService  
  

## Methods ##

### newChannelFromURIWithProxyFlags2(aURI, aProxyURI, aProxyFlags, aLoadingNode, aLoadingPrincipal, aTriggeringPrincipal, aSecurityFlags, aContentPolicyType) ###
  
Creates a channel for a given URI.  
  
@param aURI nsIURI from which to make a channel  
@param aProxyURI nsIURI to use for proxy resolution. Can be null in which  
       case aURI is used  
@param aProxyFlags flags from nsIProtocolProxyService to use  
       when resolving proxies for this new channel  
@return reference to the new nsIChannel object  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>nsIURI from which to make a channel  
</td>
</tr>

<tr>
<td>aURI</td>
<td>nsIURI from which to make a channel  
</td>
</tr>

<tr>
<td>aURI</td>
<td>nsIURI from which to make a channel  
</td>
</tr>

</table>

### newChannelFromURIWithProxyFlags(aURI, aProxyURI, aProxyFlags) ###
  
Creates a channel for a given URI.  
  
@param aURI nsIURI from which to make a channel  
@param aProxyURI nsIURI to use for proxy resolution. Can be null in which  
       case aURI is used  
@param aProxyFlags flags from nsIProtocolProxyService to use  
       when resolving proxies for this new channel  
@return reference to the new nsIChannel object  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>nsIURI from which to make a channel  
</td>
</tr>

<tr>
<td>aURI</td>
<td>nsIURI from which to make a channel  
</td>
</tr>

<tr>
<td>aURI</td>
<td>nsIURI from which to make a channel  
</td>
</tr>

</table>

## Attributes ##

### manageOfflineStatus ###
  
While this is set, IOService will monitor an nsINetworkLinkService  
(if available) and set its offline status to "true" whenever  
isLinkUp is false.  
  
Applications that want to control changes to the IOService's offline  
status should set this to false, watch for network:link-status-changed  
broadcasts, and change nsIIOService::offline as they see fit. Note  
that this means during application startup, IOService may be offline  
if there is no link, until application code runs and can turn off  
this management.  
  
