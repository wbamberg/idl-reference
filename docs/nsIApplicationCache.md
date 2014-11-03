---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIApplicationCache.idl">Source file</a>
</div>

# nsIApplicationCache #
<code>  
Application caches store resources for offline use.  Each  
application cache has a unique client ID for use with  
nsICacheService::openSession() to access the cache's entries.  
  
Each entry in the application cache can be marked with a set of  
types, as discussed in the WHAT-WG offline applications  
specification.  
  
All application caches with the same group ID belong to a cache  
group.  Each group has one "active" cache that will service future  
loads.  Inactive caches will be removed from the cache when they are  
no longer referenced.  
  
</code>
## Methods ##

### initAsHandle(groupId, clientId) ###
<code>  
Init this application cache instance to just hold the group ID and  
the client ID to work just as a handle to the real cache. Used on  
content process to simplify the application cache code.  
  
</code>
### activate() ###
<code>  
Makes this cache the active application cache for this group.  
Future loads associated with this group will come from this  
cache.  Other caches from this cache group will be deactivated.  
  
</code>
### discard() ###
<code>  
Discard this application cache.  Removes all cached resources  
for this cache.  If this is the active application cache for the  
group, the group will be removed.  
  
</code>
### markEntry(key, typeBits) ###
<code>  
Adds item types to a given entry.  
  
</code>
### unmarkEntry(key, typeBits) ###
<code>  
Removes types from a given entry.  If the resulting entry has  
no types left, the entry is removed.  
  
</code>
### getTypes(key) ###
<code>  
Gets the types for a given entry.  
  
</code>
### gatherEntries(typeBits, count, keys) ###
<code>  
Returns any entries in the application cache whose type matches  
one or more of the bits in typeBits.  
  
</code>
### addNamespaces(namespaces) ###
<code>  
Add a set of namespace entries to the application cache.  
@param namespaces  
       An nsIArray of nsIApplicationCacheNamespace entries.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>namespaces</td>
<td>       An nsIArray of nsIApplicationCacheNamespace entries.  
</td>
</tr>

</table>

### getMatchingNamespace(key) ###
<code>  
Get the most specific namespace matching a given key.  
  
</code>
## Attributes ##

### manifestURI ###
  
URI of the manfiest specifying this application cache.  
/  

### groupID ###
  
The group ID for this cache group.  It is an internally generated string  
and cannot be used as manifest URL spec.  
/  

### clientID ###
  
The client ID for this application cache.  Clients can open a  
session with nsICacheService::createSession() using this client  
ID and a storage policy of STORE_OFFLINE to access this cache.  
  

### active ###
  
TRUE if the cache is the active cache for this group.  
  

### usage ###
  
The disk usage of the application cache, in bytes.  
  

### profileDirectory ###
  
If set, this offline cache is placed in a different directory  
than the current application profile.  
  

## Constants ##

### ITEM_MANIFEST ###
  
Entries in an application cache can be marked as one or more of  
the following types.  
  

### ITEM_EXPLICIT ###

### ITEM_IMPLICIT ###

### ITEM_DYNAMIC ###

### ITEM_FOREIGN ###

### ITEM_FALLBACK ###

### ITEM_OPPORTUNISTIC ###
