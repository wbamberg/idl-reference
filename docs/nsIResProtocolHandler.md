---
layout: default
---

# nsIResProtocolHandler #
  
Protocol handler interface for the resource:// protocol  
  

## Methods ##

### setSubstitution ###
  
Sets the substitution for the root key:  
  resource://root/path ==> baseURI.resolve(path)  
  
A null baseURI removes the specified substitution.  
  
A root key should always be lowercase; however, this may not be  
enforced.  
  

### getSubstitution ###
  
Gets the substitution for the root key.  
  
@throws NS_ERROR_NOT_AVAILABLE if none exists.  
  

### hasSubstitution ###
  
Returns TRUE if the substitution exists and FALSE otherwise.  
  

### resolveURI ###
  
Utility function to resolve a resource URI.  A resolved URI is not   
guaranteed to reference a resource that exists (ie. opening a channel to  
the resolved URI may fail).  
  
@throws NS_ERROR_NOT_AVAILABLE if resURI.host() is an unknown root key.  
  
