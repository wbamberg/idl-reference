---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache2/nsICacheStorage.idl">Source file</a>
</div>

# nsICacheStorage #
<pre>  
Representation of a cache storage. There can be just-in-mem,  
in-mem+on-disk, in-mem+on-disk+app-cache or just a specific  
app-cache storage.  
  
</pre>
## Methods ##

### asyncOpenURI(aURI, aIdExtension, aFlags, aCallback) ###
<pre>  
Asynchronously opens a cache entry for the specified URI.  
Result is fetched asynchronously via the callback.  
  
@param aURI  
   The URI to search in cache or to open for writting.  
@param aIdExtension  
   Any string that will extend (distinguish) the entry.  Two entries  
   with the same aURI but different aIdExtension will be comletely  
   different entries.  If you don't know what aIdExtension should be  
   leave it empty.  
@param aFlags  
   OPEN_NORMALLY - open cache entry normally for read and write  
   OPEN_TRUNCATE - delete any existing entry before opening it  
   OPEN_READONLY - don't create an entry if there is none  
   OPEN_PRIORITY - give this request a priority over others  
   OPEN_BYPASS_IF_BUSY - backward compatibility only, LOAD_BYPASS_LOCAL_CACHE_IF_BUSY  
   CHECK_MULTITHREADED - onCacheEntryCheck may be called on any thread, consumer   
                         implementation is thread-safe  
@param aCallback  
   The consumer that receives the result.  
   IMPORTANT: The callback may be called sooner the method returns.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>   The URI to search in cache or to open for writting.  
</td>
</tr>

<tr>
<td>aIdExtension</td>
<td>   Any string that will extend (distinguish) the entry.  Two entries  
   with the same aURI but different aIdExtension will be comletely  
   different entries.  If you don't know what aIdExtension should be  
   leave it empty.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>   OPEN_NORMALLY - open cache entry normally for read and write  
   OPEN_TRUNCATE - delete any existing entry before opening it  
   OPEN_READONLY - don't create an entry if there is none  
   OPEN_PRIORITY - give this request a priority over others  
   OPEN_BYPASS_IF_BUSY - backward compatibility only, LOAD_BYPASS_LOCAL_CACHE_IF_BUSY  
   CHECK_MULTITHREADED - onCacheEntryCheck may be called on any thread, consumer   
                         implementation is thread-safe  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>   The consumer that receives the result.  
   IMPORTANT: The callback may be called sooner the method returns.  
</td>
</tr>

</table>

### openTruncate(aURI, aIdExtension) ###
<pre>  
Immediately opens a new and empty cache entry in the storage, any existing  
entries are immediately doomed.  This is similar to the recreate() method  
on nsICacheEntry.  
  
Storage may not implement this method and throw NS_ERROR_NOT_IMPLEMENTED.  
In that case consumer must use asyncOpen with OPEN_TRUNCATE flag and get  
the new entry via a callback.  
  
@param aURI @see asyncOpenURI  
@param aIdExtension @see asyncOpenURI  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>@see asyncOpenURI  
</td>
</tr>

<tr>
<td>aIdExtension</td>
<td>@see asyncOpenURI  
</td>
</tr>

</table>

### exists(aURI, aIdExtension) ###
<pre>  
Synchronously check on existance of an entry.  In case of disk entries  
this uses information from the cache index.  When the index data are not  
up to date or index is still building, NS_ERROR_NOT_AVAILABLE is thrown.  
The same error may throw any storage implementation that cannot determine  
entry state without blocking the caller.  
  
</pre>
### asyncDoomURI(aURI, aIdExtension, aCallback) ###
<pre>  
Asynchronously removes an entry belonging to the URI from the cache.  
  
</pre>
### asyncEvictStorage(aCallback) ###
<pre>  
Asynchronously removes all cached entries under this storage.  
NOTE: Disk storage also evicts memory storage.  
  
</pre>
### asyncVisitStorage(aVisitor, aVisitEntries) ###
<pre>  
Visits the storage and its entries.  
NOTE: Disk storage also visits memory storage.  
  
</pre>
## Constants ##

### OPEN_NORMALLY ###
<pre>  
Placeholder for specifying "no special flags" during open.  
  
</pre>
### OPEN_TRUNCATE ###
<pre>  
Rewrite any existing data when opening a URL.  
  
</pre>
### OPEN_READONLY ###
<pre>  
Only open an existing entry.  Don't create a new one.  
  
</pre>
### OPEN_PRIORITY ###
<pre>  
Use for first-paint blocking loads.  
  
</pre>
### OPEN_BYPASS_IF_BUSY ###
<pre>  
Bypass the cache load when write is still in progress.  
  
</pre>
### CHECK_MULTITHREADED ###
<pre>  
Perform the cache entry check (onCacheEntryCheck invocation) on any thread   
for optimal perfomance optimization.  If this flag is not specified it is  
ensured that onCacheEntryCheck is called on the same thread as respective   
asyncOpen has been called.  
  
</pre>
### OPEN_SECRETLY ###
<pre>  
Don't automatically update any 'last used' metadata of the entry.  
  
</pre>