---
layout: default
---

# nsIApplicationCacheNamespace #

Application caches can store a set of namespace entries that affect
loads from the application cache.  If a load from the cache fails
to match an exact cache entry, namespaces entries will be searched
for a substring match, and should be applied appropriately.


## NAMESPACE_BYPASS ##

Items matching this namespace can be fetched from the network
when loading from this cache.  The "data" attribute is unused.


## NAMESPACE_FALLBACK ##

Items matching this namespace can be fetched from the network
when loading from this cache.  If the load fails, the cache entry
specified by the "data" attribute should be loaded instead.


## NAMESPACE_OPPORTUNISTIC ##

Items matching this namespace should be cached
opportunistically.  Successful toplevel loads of documents
in this namespace should be placed in the application cache.
Namespaces specifying NAMESPACE_OPPORTUNISTIC may also specify
NAMESPACE_FALLBACK to supply a fallback entry.


## init ##

Initialize the namespace.


## itemType ##

The namespace type.


## namespaceSpec ##

The prefix of this namespace.  This should be the asciiSpec of the
URI prefix.


## data ##

Data associated with this namespace, such as a fallback.  URI data should
use the asciiSpec of the URI.

