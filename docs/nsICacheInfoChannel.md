---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsICacheInfoChannel.idl">Source file</a>
</div>

# nsICacheInfoChannel #

## Methods ##

### isFromCache() ###
<pre>  
TRUE if this channel's data is being loaded from the cache.  This value  
is undefined before the channel fires its OnStartRequest notification  
and after the channel fires its OnStopRequest notification.  
  
</pre>
## Attributes ##

### cacheTokenExpirationTime ###
<pre>  
Get expiration time from cache token. This attribute is equivalent to  
nsICachingChannel.cacheToken.expirationTime.  
  
</pre>
### cacheTokenCachedCharset ###
<pre>  
Set/get charset of cache entry. Accessing this attribute is equivalent to  
calling nsICachingChannel.cacheToken.getMetaDataElement("charset") and  
nsICachingChannel.cacheToken.setMetaDataElement("charset").  
  
</pre>