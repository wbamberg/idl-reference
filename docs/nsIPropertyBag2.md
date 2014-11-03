---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIPropertyBag2.idl">Source file</a>
</div>

# nsIPropertyBag2 #

## Methods ##

### getPropertyAsInt32(prop) ###

### getPropertyAsUint32(prop) ###

### getPropertyAsInt64(prop) ###

### getPropertyAsUint64(prop) ###

### getPropertyAsDouble(prop) ###

### getPropertyAsAString(prop) ###

### getPropertyAsACString(prop) ###

### getPropertyAsAUTF8String(prop) ###

### getPropertyAsBool(prop) ###

### getPropertyAsInterface(prop, iid, result) ###
<code>  
This method returns null if the value exists, but is null.  
  
</code>
### get(prop) ###
<code>  
This method returns null if the value does not exist,  
or exists but is null.  
  
</code>
### hasKey(prop) ###
<code>  
Check for the existence of a key.  
  
</code>