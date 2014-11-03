---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIWeakReference.idl">Source file</a>
</div>

# nsISupportsWeakReference #
  
|nsISupportsWeakReference| is a factory interface which produces appropriate  
instances of |nsIWeakReference|.  Weak references in this scheme can only be  
produced for objects that implement this interface.  
  
@version 1.0  
@see nsIWeakReference  
@see nsSupportsWeakReference  
  

## Methods ##

### GetWeakReference() ###
  
|GetWeakReference| produces an appropriate instance of |nsIWeakReference|.  
As with all good XPCOM `getters', you own the resulting interface and should  
manage it with an |nsCOMPtr|.  
  
@see nsIWeakReference  
@see nsWeakPtr  
@see nsCOMPtr  
  
