---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIApplicationCache.idl">Source file</a>
</div>

# nsIApplicationCache #
<pre>  
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
  
</pre>
## Methods ##

### initAsHandle(groupId, clientId) ###
<pre>  
Init this application cache instance to just hold the group ID and  
the client ID to work just as a handle to the real cache. Used on  
content process to simplify the application cache code.  
  
</pre>
### activate() ###
<pre>  
Makes this cache the active application cache for this group.  
Future loads associated with this group will come from this  
cache.  Other caches from this cache group will be deactivated.  
  
</pre>
### discard() ###
<pre>  
Discard this application cache.  Removes all cached resources  
for this cache.  If this is the active application cache for the  
group, the group will be removed.  
  
</pre>
### markEntry(key, typeBits) ###
<pre>  
Adds item types to a given entry.  
  
</pre>
### unmarkEntry(key, typeBits) ###
<pre>  
Removes types from a given entry.  If the resulting entry has  
no types left, the entry is removed.  
  
</pre>
### getTypes(key) ###
<pre>  
Gets the types for a given entry.  
  
</pre>
### gatherEntries(typeBits, count, keys) ###
<pre>  
Returns any entries in the application cache whose type matches  
one or more of the bits in typeBits.  
  
</pre>
### addNamespaces(namespaces) ###
<pre>  
Add a set of namespace entries to the application cache.  
@param namespaces  
       An nsIArray of nsIApplicationCacheNamespace entries.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>namespaces</td>
<td>       An nsIArray of nsIApplicationCacheNamespace entries.  
</td>
</tr>

</table>

### getMatchingNamespace(key) ###
<pre>  
Get the most specific namespace matching a given key.  
  
</pre>
## Attributes ##

### manifestURI ###
<pre>  
URI of the manfiest specifying this application cache.  
/  
</pre>
### groupID ###
<pre>  
The group ID for this cache group.  It is an internally generated string  
and cannot be used as manifest URL spec.  
/  
</pre>
### clientID ###
<pre>  
The client ID for this application cache.  Clients can open a  
session with nsICacheService::createSession() using this client  
ID and a storage policy of STORE_OFFLINE to access this cache.  
  
</pre>
### active ###
<pre>  
TRUE if the cache is the active cache for this group.  
  
</pre>
### usage ###
<pre>  
The disk usage of the application cache, in bytes.  
  
</pre>
### profileDirectory ###
<pre>  
If set, this offline cache is placed in a different directory  
than the current application profile.  
  
</pre>
## Constants ##

### ITEM_MANIFEST ###
<pre>  
Entries in an application cache can be marked as one or more of  
the following types.  
  
</pre>
### ITEM_EXPLICIT ###

### ITEM_IMPLICIT ###

### ITEM_DYNAMIC ###

### ITEM_FOREIGN ###

### ITEM_FALLBACK ###

### ITEM_OPPORTUNISTIC ###
