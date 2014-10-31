---
layout: default
---

# nsICacheService #
  
@deprecated  
  
IMPORTANT NOTE: THIS INTERFACE IS NO LONGER SUPPORTED AND PLANNED TO BE  
REMOVED SOON. WE STRONGLY ENCORAGE TO MIGRATE THE EXISTING CODE AND FOR  
THE NEW CODE USE ONLY THE NEW HTTP CACHE API IN netwerk/cache2/.  
  

## Methods ##

### createSession(clientID, storagePolicy, streamBased) ###
  
@throws NS_ERROR_NOT_IMPLEMENTED when the cache v2 is prefered to use.  
  
Create a cache session  
  
A cache session represents a client's access into the cache.  The cache  
session is not "owned" by the cache service.  Hence, it is possible to  
create duplicate cache sessions.  Entries created by a cache session  
are invisible to other cache sessions, unless the cache sessions are  
equivalent.  
  
@param clientID - Specifies the name of the client using the cache.  
@param storagePolicy - Limits the storage policy for all entries  
  accessed via the returned session.  As a result, devices excluded  
  by the storage policy will not be searched when opening entries  
  from the returned session.  
@param streamBased - Indicates whether or not the data being cached  
  can be represented as a stream.  The storagePolicy must be   
  consistent with the value of this field.  For example, a non-stream-  
  based cache entry can only have a storage policy of STORE_IN_MEMORY.  
@return new cache session.  
  

#### Parameters ####

<table>

<tr>
<td>clientID</td>
<td>- Specifies the name of the client using the cache.  
</td>
</tr>

<tr>
<td>clientID</td>
<td>- Specifies the name of the client using the cache.  
</td>
</tr>

<tr>
<td>clientID</td>
<td>- Specifies the name of the client using the cache.  
</td>
</tr>

</table>

### visitEntries(visitor) ###
  
@throws NS_ERROR_NOT_IMPLEMENTED when the cache v2 is prefered to use.  
  
Visit entries stored in the cache.  Used to implement about:cache.  
  

### evictEntries(storagePolicy) ###
  
@throws NS_ERROR_NOT_IMPLEMENTED when the cache v2 is prefered to use.  
  
Evicts all entries in all devices implied by the storage policy.  
  
@note This function may evict some items but will throw if it fails to evict  
      everything.  
  

## Attributes ##

### cacheIOTarget ###
  
Event target which is used for I/O operations  
  
