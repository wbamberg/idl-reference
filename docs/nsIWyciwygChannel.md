---
layout: default
---

# nsIWyciwygChannel #
  
A channel to  manage all cache-related interactions for layout  
when it is dealing with dynamic pages created through   
document.write(). This interface provides methods that will  
help layout save dynamic pages in cache for future retrievals.  
  

## Methods ##

### writeToCacheEntry ###
  
Append data to the cache entry; opens the cache entry if necessary.  
  

### closeCacheEntry ###
  
Close the cache entry; subsequent writes have undefined behavior.  
  

### setSecurityInfo ###
  
Set the wyciwyg channels security info  
  

### setCharsetAndSource ###
  
Store and read a charset and charset source on the wyciwyg channel.  These  
are opaque values to the channel; consumers who set them should know what  
they mean.  
  

### getCharsetAndSource ###
  
The return value is the charset.  Throws if either the charset or the  
source cannot be retrieved.  This is guaranteed to return a nonzero source  
and a nonempty charset if it does not throw.  
  
