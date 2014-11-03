---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/res/nsIResProtocolHandler.idl">Source file</a>
</div>

# nsIResProtocolHandler #
  
Protocol handler interface for the resource:// protocol  
  

## Methods ##

### setSubstitution(root, baseURI) ###
  
Sets the substitution for the root key:  
  resource://root/path ==> baseURI.resolve(path)  
  
A null baseURI removes the specified substitution.  
  
A root key should always be lowercase; however, this may not be  
enforced.  
  

### getSubstitution(root) ###
  
Gets the substitution for the root key.  
  
@throws NS_ERROR_NOT_AVAILABLE if none exists.  
  

### hasSubstitution(root) ###
  
Returns TRUE if the substitution exists and FALSE otherwise.  
  

### resolveURI(resURI) ###
  
Utility function to resolve a resource URI.  A resolved URI is not   
guaranteed to reference a resource that exists (ie. opening a channel to  
the resolved URI may fail).  
  
@throws NS_ERROR_NOT_AVAILABLE if resURI.host() is an unknown root key.  
  
