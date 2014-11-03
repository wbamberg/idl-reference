---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache/nsICacheSession.idl">Source file</a>
</div>

# nsICacheSession #

## Methods ##

### openCacheEntry(key, accessRequested, blockingMode) ###
<code>  
A cache session can only give out one descriptor with WRITE access  
to a given cache entry at a time.  Until the client calls MarkValid on  
its descriptor, other attempts to open the same cache entry will block.  
  
</code><code>  
Synchronous cache access. This method fails if it is called on the main  
thread. Use asyncOpenCacheEntry() instead. This returns a unique  
descriptor each time it is called, even if the same key is specified.  
When called by multiple threads for write access, only one writable  
descriptor will be granted.  If 'blockingMode' is set to false, it will  
return NS_ERROR_CACHE_WAIT_FOR_VALIDATION rather than block when another  
descriptor has been given WRITE access but hasn't validated the entry yet.  
  
</code>
### asyncOpenCacheEntry(key, accessRequested, listener, noWait) ###
<code>  
Asynchronous cache access. Does not block the calling thread. Instead,  
the listener will be notified when the descriptor is available. If  
'noWait' is set to true, the listener will be notified immediately with  
status NS_ERROR_CACHE_WAIT_FOR_VALIDATION rather than queuing the request  
when another descriptor has been given WRITE access but hasn't validated  
the entry yet.  
  
</code>
### evictEntries() ###
<code>  
Evict all entries for this session's clientID according to its storagePolicy.  
  
</code>
### isStorageEnabled() ###
<code>  
Return whether any of the cache devices implied by the session storage policy  
are currently enabled for instantiation if they don't already exist.  
  
</code>
### doomEntry(key, listener) ###
<code>  
Asynchronously doom an entry specified by the key. Listener will be  
notified about the status of the operation. Null may be passed if caller  
doesn't care about the result.  
  
</code>
## Attributes ##

### doomEntriesIfExpired ###
  
Expired entries will be doomed or evicted if this attribute is set to  
true.  If false, expired entries will be returned (useful for offline-  
mode and clients, such as HTTP, that can update the valid lifetime of  
cached content).  This attribute defaults to true.  
  

### profileDirectory ###
  
When set, entries created with this session will be placed to a cache  
based at this directory.  Use when storing entries to a different  
profile than the active profile of the the current running application  
process.  
  

### isPrivate ###
  
Private entries will be doomed when the last private browsing session  
finishes.  
  
