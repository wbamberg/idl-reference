---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache2/nsICacheStorageService.idl">Source file</a>
</div>
# nsICacheStorageService #
  
Provides access to particual cache storages of the network URI cache.  
  

## Methods ##

### memoryCacheStorage(aLoadContextInfo) ###
  
Get storage where entries will only remain in memory, never written  
to the disk.  
  
NOTE: Any existing disk entry for [URL|id-extension] will be doomed  
prior opening an entry using this memory-only storage.  Result of  
AsyncOpenURI will be a new and empty memory-only entry.  Using  
OPEN_READONLY open flag has no effect on this behavior.  
  
@param aLoadContextInfo  
   Information about the loading context, this focuses the storage JAR and  
   respects separate storage for private browsing.  
  

#### Parameters ####

<table>

<tr>
<td>aLoadContextInfo</td>
<td>   Information about the loading context, this focuses the storage JAR and  
   respects separate storage for private browsing.  
</td>
</tr>

</table>

### diskCacheStorage(aLoadContextInfo, aLookupAppCache) ###
  
Get storage where entries will be written to disk when not forbidden by  
response headers.  
  
@param aLookupAppCache  
   When set true (for top level document loading channels) app cache will  
   be first to check on to find entries in.  
  

#### Parameters ####

<table>

<tr>
<td>aLookupAppCache</td>
<td>   When set true (for top level document loading channels) app cache will  
   be first to check on to find entries in.  
</td>
</tr>

</table>

### appCacheStorage(aLoadContextInfo, aApplicationCache) ###
  
Get storage for a specified application cache obtained using some different  
mechanism.  
  
@param aLoadContextInfo  
   Mandatory reference to a load context information.  
@param aApplicationCache  
   Optional reference to an existing appcache.  When left null, this will  
   work with offline cache as a whole.  
  

#### Parameters ####

<table>

<tr>
<td>aLoadContextInfo</td>
<td>   Mandatory reference to a load context information.  
</td>
</tr>

<tr>
<td>aApplicationCache</td>
<td>   Optional reference to an existing appcache.  When left null, this will  
   work with offline cache as a whole.  
</td>
</tr>

</table>

### clear() ###
  
Evict the whole cache.  
  

### purgeFromMemory(aWhat) ###
  
Purges data we keep warmed in memory.  Use for tests and for  
saving memory.  
  

### asyncGetDiskConsumption(aObserver) ###
  
Asynchronously determine how many bytes of the disk space the cache takes.  
@see nsICacheStorageConsumptionObserver  
@param aObserver  
   A mandatory (weak referred) observer.  Documented at  
   nsICacheStorageConsumptionObserver.  
   NOTE: the observer MUST implement nsISupportsWeakReference.  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>   A mandatory (weak referred) observer.  Documented at  
   nsICacheStorageConsumptionObserver.  
   NOTE: the observer MUST implement nsISupportsWeakReference.  
</td>
</tr>

</table>

## Attributes ##

### ioTarget ###
  
I/O thread target to use for any operations on disk  
  

## Constants ##

### PURGE_DISK_DATA_ONLY ###
  
Purge only data of disk backed entries.  Metadata are left for  
performance purposes.  
  

### PURGE_DISK_ALL ###
  
Purge whole disk backed entries from memory.  Disk files will  
be left unattended.  
  

### PURGE_EVERYTHING ###
  
Purge all entries we keep in memory, including memory-storage  
entries.  This may be dangerous to use.  
  
