---
layout: default
---

# nsICacheStorage #

Representation of a cache storage. There can be just-in-mem,
in-mem+on-disk, in-mem+on-disk+app-cache or just a specific
app-cache storage.


## OPEN_NORMALLY ##

Placeholder for specifying "no special flags" during open.


## OPEN_TRUNCATE ##

Rewrite any existing data when opening a URL.


## OPEN_READONLY ##

Only open an existing entry.  Don't create a new one.


## OPEN_PRIORITY ##

Use for first-paint blocking loads.


## OPEN_BYPASS_IF_BUSY ##

Bypass the cache load when write is still in progress.


## CHECK_MULTITHREADED ##

Perform the cache entry check (onCacheEntryCheck invocation) on any thread 
for optimal perfomance optimization.  If this flag is not specified it is
ensured that onCacheEntryCheck is called on the same thread as respective 
asyncOpen has been called.


## OPEN_SECRETLY ##

Don't automatically update any 'last used' metadata of the entry.


## asyncOpenURI ##

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


## openTruncate ##

Immediately opens a new and empty cache entry in the storage, any existing
entries are immediately doomed.  This is similar to the recreate() method
on nsICacheEntry.

Storage may not implement this method and throw NS_ERROR_NOT_IMPLEMENTED.
In that case consumer must use asyncOpen with OPEN_TRUNCATE flag and get
the new entry via a callback.

@param aURI @see asyncOpenURI
@param aIdExtension @see asyncOpenURI


## exists ##

Synchronously check on existance of an entry.  In case of disk entries
this uses information from the cache index.  When the index data are not
up to date or index is still building, NS_ERROR_NOT_AVAILABLE is thrown.
The same error may throw any storage implementation that cannot determine
entry state without blocking the caller.


## asyncDoomURI ##

Asynchronously removes an entry belonging to the URI from the cache.


## asyncEvictStorage ##

Asynchronously removes all cached entries under this storage.
NOTE: Disk storage also evicts memory storage.


## asyncVisitStorage ##

Visits the storage and its entries.
NOTE: Disk storage also visits memory storage.

