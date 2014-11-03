---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/wyciwyg/nsIWyciwygChannel.idl">Source file</a>
</div>

# nsIWyciwygChannel #
<code>  
A channel to  manage all cache-related interactions for layout  
when it is dealing with dynamic pages created through   
document.write(). This interface provides methods that will  
help layout save dynamic pages in cache for future retrievals.  
  
</code>
## Methods ##

### writeToCacheEntry(aData) ###
<code>  
Append data to the cache entry; opens the cache entry if necessary.  
  
</code>
### closeCacheEntry(reason) ###
<code>  
Close the cache entry; subsequent writes have undefined behavior.  
  
</code>
### setSecurityInfo(aSecurityInfo) ###
<code>  
Set the wyciwyg channels security info  
  
</code>
### setCharsetAndSource(aSource, aCharset) ###
<code>  
Store and read a charset and charset source on the wyciwyg channel.  These  
are opaque values to the channel; consumers who set them should know what  
they mean.  
  
</code>
### getCharsetAndSource(aSource) ###
<code>  
The return value is the charset.  Throws if either the charset or the  
source cannot be retrieved.  This is guaranteed to return a nonzero source  
and a nonempty charset if it does not throw.  
  
</code>