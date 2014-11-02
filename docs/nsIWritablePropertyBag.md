---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIWritablePropertyBag.idl">Source file</a>
</div>

# nsIWritablePropertyBag #

## Methods ##

### setProperty(name, value) ###
  
Set a property with the given name to the given value.  If  
a property already exists with the given name, it is  
overwritten.  
  

### deleteProperty(name) ###
  
Delete a property with the given name.  
@throws NS_ERROR_FAILURE if a property with that name doesn't  
exist.  
  
