---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/cache/nsICacheVisitor.idl">Source file</a>
</div>

# nsICacheEntryInfo #

## Methods ##

### isStreamBased() ###
<pre>  
Find out whether or not the cache entry is stream based.  
  
</pre>
## Attributes ##

### clientID ###
<pre>  
Get the client id associated with this cache entry.  
  
</pre>
### deviceID ###
<pre>  
Get the id for the device that stores this cache entry.  
  
</pre>
### key ###
<pre>  
Get the key identifying the cache entry.  
  
</pre>
### fetchCount ###
<pre>  
Get the number of times the cache entry has been opened.  
  
</pre>
### lastFetched ###
<pre>  
Get the last time the cache entry was opened (in seconds since the Epoch).  
  
</pre>
### lastModified ###
<pre>  
Get the last time the cache entry was modified (in seconds since the Epoch).  
  
</pre>
### expirationTime ###
<pre>  
Get the expiration time of the cache entry (in seconds since the Epoch).  
  
</pre>
### dataSize ###
<pre>  
Get the cache entry data size.  
  
</pre>