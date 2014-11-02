---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsICacheInfoChannel.idl">Source file</a>
</div>
# nsICacheInfoChannel #

## Methods ##

### isFromCache() ###
  
TRUE if this channel's data is being loaded from the cache.  This value  
is undefined before the channel fires its OnStartRequest notification  
and after the channel fires its OnStopRequest notification.  
  

## Attributes ##

### cacheTokenExpirationTime ###
  
Get expiration time from cache token. This attribute is equivalent to  
nsICachingChannel.cacheToken.expirationTime.  
  

### cacheTokenCachedCharset ###
  
Set/get charset of cache entry. Accessing this attribute is equivalent to  
calling nsICachingChannel.cacheToken.getMetaDataElement("charset") and  
nsICachingChannel.cacheToken.setMetaDataElement("charset").  
  
