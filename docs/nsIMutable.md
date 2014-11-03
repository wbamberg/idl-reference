---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIMutable.idl">Source file</a>
</div>

# nsIMutable #
<code>  
nsIMutable defines an interface to be implemented by objects which  
can be made immutable.  
  
</code>
## Attributes ##

### mutable ###
  
Control whether or not this object can be modified.  If the flag is  
false, no modification is allowed.  Once the flag has been set to false,  
it cannot be reset back to true -- attempts to do so throw  
NS_ERROR_INVALID_ARG.  
  
