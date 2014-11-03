---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache/nsICacheEntryDescriptor.idl">Source file</a>
</div>

# nsICacheEntryDescriptor #

## Methods ##

### setExpirationTime(expirationTime) ###
<pre>  
Set the time at which the cache entry should be considered invalid (in  
seconds since the Epoch).  
  
</pre>
### setDataSize(size) ###
<pre>  
Set the cache entry data size.  This will fail if the cache entry  
IS stream based.  
  
</pre>
### openInputStream(offset) ###
<pre>  
Open blocking input stream to cache data.  This will fail if the cache  
entry IS NOT stream based.  Use the stream transport service to  
asynchronously read this stream on a background thread.  The returned  
stream MAY implement nsISeekableStream.  
  
@param offset  
       read starting from this offset into the cached data.  an offset  
       beyond the end of the stream has undefined consequences.  
  
@return blocking, unbuffered input stream.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>offset</td>
<td>       read starting from this offset into the cached data.  an offset  
       beyond the end of the stream has undefined consequences.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>blocking, unbuffered input stream.  
</td>
</tr>

</table>

### openOutputStream(offset) ###
<pre>  
Open blocking output stream to cache data.  This will fail if the cache  
entry IS NOT stream based.  Use the stream transport service to  
asynchronously write to this stream on a background thread.  The returned  
stream MAY implement nsISeekableStream.  
  
If opening an output stream to existing cached data, the data will be  
truncated to the specified offset.  
  
@param offset  
       write starting from this offset into the cached data.  an offset  
       beyond the end of the stream has undefined consequences.  
  
@return blocking, unbuffered output stream.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>offset</td>
<td>       write starting from this offset into the cached data.  an offset  
       beyond the end of the stream has undefined consequences.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>blocking, unbuffered output stream.  
</td>
</tr>

</table>

### doom() ###
<pre>  
Doom the cache entry this descriptor references in order to slate it for   
removal.  Once doomed a cache entry cannot be undoomed.  
  
A descriptor with WRITE access can doom the cache entry and choose to  
fail pending requests.  This means that pending requests will not get  
a cache descriptor.  This is meant as a tool for clients that wish to  
instruct pending requests to skip the cache.  
  
</pre>
### doomAndFailPendingRequests(status) ###

### asyncDoom(listener) ###
<pre>  
Asynchronously doom an entry. Listener will be notified about the status  
of the operation. Null may be passed if caller doesn't care about the  
result.  
  
</pre>
### markValid() ###
<pre>  
A writer must validate this cache object before any readers are given  
a descriptor to the object.  
  
</pre>
### close() ###
<pre>  
 Explicitly close the descriptor (optional).  
  
</pre>
### getMetaDataElement(key) ###
<pre>  
Methods for accessing meta data.  Meta data is a table of key/value  
string pairs.  The strings do not have to conform to any particular  
charset, but they must be null terminated.  
  
</pre>
### setMetaDataElement(key, value) ###

### visitMetaData(visitor) ###
<pre>  
Visitor will be called with key/value pair for each meta data element.  
  
</pre>
## Attributes ##

### cacheElement ###
<pre>  
Get/set the cache data element.  This will fail if the cache entry  
IS stream based.  The cache entry holds a strong reference to this  
object.  The object will be released when the cache entry is destroyed.  
  
</pre>
### predictedDataSize ###
<pre>  
Stores the Content-Length specified in the HTTP header for this  
entry. Checked before we write to the cache entry, to prevent ever  
taking up space in the cache for an entry that we know up front   
is going to have to be evicted anyway. See bug 588507.  
  
</pre>
### accessGranted ###
<pre>  
Get the access granted to this descriptor.  See nsICache.idl for the  
definitions of the access modes and a thorough description of their  
corresponding meanings.  
  
</pre>
### storagePolicy ###
<pre>  
Get/set the storage policy of the cache entry.  See nsICache.idl for  
the definitions of the storage policies.  
  
</pre>
### file ###
<pre>  
Get the disk file associated with the cache entry.  
  
</pre>
### securityInfo ###
<pre>  
Get/set security info on the cache entry for this descriptor.  This fails  
if the storage policy is not STORE_IN_MEMORY.  
  
</pre>
### storageDataSize ###
<pre>  
Get the size of the cache entry data, as stored. This may differ  
from the entry's dataSize, if the entry is compressed.  
  
</pre>