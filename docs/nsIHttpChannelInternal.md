---
layout: default
---

# nsIHttpChannelInternal #
  
Dumping ground for http.  This interface will never be frozen.  If you are  
using any feature exposed by this interface, be aware that this interface  
will change and you will be broken.  You have been warned.  
  

## Methods ##

### getRequestVersion(major, minor) ###
  
Get the major/minor version numbers for the request  
  

### getResponseVersion(major, minor) ###
  
Get the major/minor version numbers for the response  
  

### takeAllSecurityMessages(aMessages) ###

### setCookie(aCookieHeader) ###
  
Helper method to set a cookie with a consumer-provided  
cookie header, _but_ using the channel's other information  
(URI's, prompters, date headers etc).  
  
@param aCookieHeader  
       The cookie header to be parsed.  
  

#### Parameters ####

<table>

<tr>
<td>aCookieHeader</td>
<td>       The cookie header to be parsed.  
</td>
</tr>

</table>

### setupFallbackChannel(aFallbackKey) ###
  
Setup this channel as an application cache fallback channel.  
  

### setCacheKeysRedirectChain(cacheKeys) ###
  
Transfer chain of redirected cache-keys.  
  

### HTTPUpgrade(aProtocolName, aListener) ###
  
HTTPUpgrade allows for the use of HTTP to bootstrap another protocol  
via the RFC 2616 Upgrade request header in conjunction with a 101 level  
response. The nsIHttpUpgradeListener will have its  
onTransportAvailable() method invoked if a matching 101 is processed.  
The arguments to onTransportAvailable provide the new protocol the low  
level tranport streams that are no longer used by HTTP.  
  
The onStartRequest and onStopRequest events are still delivered and the  
listener gets full control over the socket if and when onTransportAvailable  
is delievered.  
  
@param aProtocolName  
       The value of the HTTP Upgrade request header  
@param aListener  
       The callback object used to handle a successful upgrade  
  

#### Parameters ####

<table>

<tr>
<td>aProtocolName</td>
<td>       The value of the HTTP Upgrade request header  
</td>
</tr>

<tr>
<td>aProtocolName</td>
<td>       The value of the HTTP Upgrade request header  
</td>
</tr>

</table>

### addRedirect(aPrincipal) ###
  
Add a new nsIPrincipal to the redirect chain. This is the only way to  
write to nsIRedirectHistory.redirects.  
  

### forceNoIntercept() ###
  
Force a channel that has not been AsyncOpen'ed to skip any check for possible  
interception and proceed immediately to the network/cache.  
  

## Attributes ##

### documentURI ###
  
An http channel can own a reference to the document URI  
  

### forceAllowThirdPartyCookie ###
  
Force relevant cookies to be sent with this load even if normally they  
wouldn't be.  
  

### canceled ###
  
True iff the channel has been canceled.  
  

### channelIsForDownload ###
  
External handlers may set this to true to notify the channel  
that it is open on behalf of a download.  
  

### localAddress ###
  
The local IP address to which this channel is bound, in the  
format produced by PR_NetAddrToString. May be IPv4 or IPv6.  
Note: in the presence of NAT, this may not be the same as the  
address that the remote host thinks it's talking to.  
  
May throw NS_ERROR_NOT_AVAILABLE if accessed when the channel's  
endpoints are not yet determined, or in any case when  
nsIHttpActivityObserver.isActive is false. See bugs 534698 and 526207.  
  

### localPort ###
  
The local port number to which this channel is bound.  
  
May throw NS_ERROR_NOT_AVAILABLE if accessed when the channel's  
endpoints are not yet determined, or in any case when  
nsIHttpActivityObserver.isActive is false. See bugs 534698 and 526207.  
  

### remoteAddress ###
  
The IP address of the remote host that this channel is  
connected to, in the format produced by PR_NetAddrToString.  
  
May throw NS_ERROR_NOT_AVAILABLE if accessed when the channel's  
endpoints are not yet determined, or in any case when  
nsIHttpActivityObserver.isActive is false. See bugs 534698 and 526207.  
  

### remotePort ###
  
The remote port number that this channel is connected to.  
  
May throw NS_ERROR_NOT_AVAILABLE if accessed when the channel's  
endpoints are not yet determined, or in any case when  
nsIHttpActivityObserver.isActive is false. See bugs 534698 and 526207.  
  

### allowSpdy ###
  
Enable/Disable Spdy negotiation on per channel basis.  
The network.http.spdy.enabled preference is still a pre-requisite  
for starting spdy.  
  

### loadAsBlocking ###
  
Set (e.g., by the docshell) to indicate whether or not the channel  
corresponds to content that should be given a degree of network exclusivity  
with respect to other members of its load group.  
Examples are js from the HTML head and css which are latency  
sensitive and should not compete with images for bandwidth. Default false.  
  

### loadUnblocked ###
  
If set, this channel will load in parallel with the rest of the load  
group even if a blocking subset of the group would normally be given  
exclusivity. Default false.  
  

### responseTimeoutEnabled ###
  
This attribute en/disables the timeout for the first byte of an HTTP  
response. Enabled by default.  
  

### apiRedirectToURI ###
  
Get value of the URI passed to nsIHttpChannel.redirectTo() if any.  
May return null when redirectTo() has not been called.  
  

### lastModifiedTime ###
