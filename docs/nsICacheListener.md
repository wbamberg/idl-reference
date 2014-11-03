---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache/nsICacheListener.idl">Source file</a>
</div>

# nsICacheListener #

## Methods ##

### onCacheEntryAvailable(descriptor, accessGranted, status) ###
<code>  
Called when the requested access (or appropriate subset) is  
acquired.  The status parameter equals NS_OK on success.  
See nsICacheService.idl for accessGranted values.  
  
</code>
### onCacheEntryDoomed(status) ###
<code>  
Called when nsCacheSession::DoomEntry() is completed. The status  
parameter is NS_OK when the entry was doomed, or NS_ERROR_NOT_AVAILABLE  
when there is no such entry.  
  
</code>