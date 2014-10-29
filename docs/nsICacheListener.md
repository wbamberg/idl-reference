---
layout: default
---

# nsICacheListener #

## Methods ##

### onCacheEntryAvailable ###

Called when the requested access (or appropriate subset) is
acquired.  The status parameter equals NS_OK on success.
See nsICacheService.idl for accessGranted values.


### onCacheEntryDoomed ###

Called when nsCacheSession::DoomEntry() is completed. The status
parameter is NS_OK when the entry was doomed, or NS_ERROR_NOT_AVAILABLE
when there is no such entry.

