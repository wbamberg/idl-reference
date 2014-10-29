---
layout: default
---

# nsICachingChannel #

A channel may optionally implement this interface to allow clients
to affect its behavior with respect to how it uses the cache service.

This interface provides:
  1) Support for "stream as file" semantics (for JAR and plugins).
  2) Support for "pinning" cached data in the cache (for printing and save-as).
  3) Support for uniquely identifying cached data in cases when the URL
     is insufficient (e.g., HTTP form submission).


## cacheToken ##

Set/get the cache token... uniquely identifies the data in the cache.
Holding a reference to this token prevents the cached data from being
removed.

A cache token retrieved from a particular instance of nsICachingChannel
could be set on another instance of nsICachingChannel provided the
underlying implementations are compatible.  The implementation of
nsICachingChannel would be expected to only read from the cache entry
identified by the cache token and not try to validate it.

The cache token can be QI'd to a nsICacheEntryInfo if more detail
about the cache entry is needed (e.g., expiration time).


## offlineCacheToken ##

The same as above but accessing the offline app cache token if there
is any.

@throws
     NS_ERROR_NOT_AVAILABLE when there is not offline cache token


## cacheKey ##

Set/get the cache key... uniquely identifies the data in the cache
for this channel.  Holding a reference to this key does NOT prevent
the cached data from being removed.

A cache key retrieved from a particular instance of nsICachingChannel
could be set on another instance of nsICachingChannel provided the
underlying implementations are compatible and provided the new 
channel instance was created with the same URI.  The implementation of
nsICachingChannel would be expected to use the cache entry identified
by the cache token.  Depending on the value of nsIRequest::loadFlags,
the cache entry may be validated, overwritten, or simply read.

The cache key may be NULL indicating that the URI of the channel is
sufficient to locate the same cache entry.  Setting a NULL cache key
is likewise valid.


## cacheOnlyMetadata ##

Instructs the channel to only store the metadata of the entry, and not
the content. When reading an existing entry, this automatically sets
LOAD_ONLY_IF_MODIFIED flag.
Must be called before asyncOpen().


## LOAD_NO_NETWORK_IO ##
**********************************************************************
Caching channel specific load flags:


This load flag inhibits fetching from the net.  An error of
NS_ERROR_DOCUMENT_NOT_CACHED will be sent to the listener's
onStopRequest if network IO is necessary to complete the request.

This flag can be used to find out whether fetching this URL would
cause validation of the cache entry via the network.

Combining this flag with LOAD_BYPASS_LOCAL_CACHE will cause all
loads to fail. This flag differs from LOAD_ONLY_FROM_CACHE in that
this flag fails the load if validation is required while
LOAD_ONLY_FROM_CACHE skips validation where possible.


## LOAD_CHECK_OFFLINE_CACHE ##

This load flag causes the offline cache to be checked when fetching
a request.  It will be set automatically if the browser is offline.

This flag will not be transferred through a redirect.


## LOAD_BYPASS_LOCAL_CACHE ##

This load flag causes the local cache to be skipped when fetching a
request.  Unlike LOAD_BYPASS_CACHE, it does not force an end-to-end load
(i.e., it does not affect proxy caches).


## LOAD_BYPASS_LOCAL_CACHE_IF_BUSY ##

This load flag causes the local cache to be skipped if the request
would otherwise block waiting to access the cache.


## LOAD_ONLY_FROM_CACHE ##

This load flag inhibits fetching from the net if the data in the cache
has been evicted.  An error of NS_ERROR_DOCUMENT_NOT_CACHED will be sent
to the listener's onStopRequest in this case.  This flag is set
automatically when the application is offline.


## LOAD_ONLY_IF_MODIFIED ##

This load flag controls what happens when a document would be loaded
from the cache to satisfy a call to AsyncOpen.  If this attribute is
set to TRUE, then the document will not be loaded from the cache.  A
stream listener can check nsICachingChannel::isFromCache to determine
if the AsyncOpen will actually result in data being streamed.

If this flag has been set, and the request can be satisfied via the
cache, then the OnDataAvailable events will be skipped.  The listener
will only see OnStartRequest followed by OnStopRequest.

