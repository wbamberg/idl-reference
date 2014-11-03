---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIApplicationCache.idl">Source file</a>
</div>

# nsIApplicationCacheNamespace #
<pre>  
Application caches can store a set of namespace entries that affect  
loads from the application cache.  If a load from the cache fails  
to match an exact cache entry, namespaces entries will be searched  
for a substring match, and should be applied appropriately.  
  
</pre>
## Methods ##

### init(itemType, namespaceSpec, data) ###
<pre>  
Initialize the namespace.  
  
</pre>
## Attributes ##

### itemType ###
<pre>  
The namespace type.  
  
</pre>
### namespaceSpec ###
<pre>  
The prefix of this namespace.  This should be the asciiSpec of the  
URI prefix.  
  
</pre>
### data ###
<pre>  
Data associated with this namespace, such as a fallback.  URI data should  
use the asciiSpec of the URI.  
  
</pre>
## Constants ##

### NAMESPACE_BYPASS ###
<pre>  
Items matching this namespace can be fetched from the network  
when loading from this cache.  The "data" attribute is unused.  
  
</pre>
### NAMESPACE_FALLBACK ###
<pre>  
Items matching this namespace can be fetched from the network  
when loading from this cache.  If the load fails, the cache entry  
specified by the "data" attribute should be loaded instead.  
  
</pre>
### NAMESPACE_OPPORTUNISTIC ###
<pre>  
Items matching this namespace should be cached  
opportunistically.  Successful toplevel loads of documents  
in this namespace should be placed in the application cache.  
Namespaces specifying NAMESPACE_OPPORTUNISTIC may also specify  
NAMESPACE_FALLBACK to supply a fallback entry.  
  
</pre>