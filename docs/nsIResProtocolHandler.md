---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/res/nsIResProtocolHandler.idl">Source file</a>
</div>

# nsIResProtocolHandler #
<pre>  
Protocol handler interface for the resource:// protocol  
  
</pre>
## Methods ##

### setSubstitution(root, baseURI) ###
<pre>  
Sets the substitution for the root key:  
  resource://root/path ==> baseURI.resolve(path)  
  
A null baseURI removes the specified substitution.  
  
A root key should always be lowercase; however, this may not be  
enforced.  
  
</pre>
### getSubstitution(root) ###
<pre>  
Gets the substitution for the root key.  
  
@throws NS_ERROR_NOT_AVAILABLE if none exists.  
  
</pre>
### hasSubstitution(root) ###
<pre>  
Returns TRUE if the substitution exists and FALSE otherwise.  
  
</pre>
### resolveURI(resURI) ###
<pre>  
Utility function to resolve a resource URI.  A resolved URI is not   
guaranteed to reference a resource that exists (ie. opening a channel to  
the resolved URI may fail).  
  
@throws NS_ERROR_NOT_AVAILABLE if resURI.host() is an unknown root key.  
  
</pre>