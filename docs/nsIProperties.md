---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIProperties.idl">Source file</a>
</div>

# nsIProperties #

## Methods ##

### get(prop, iid, result) ###
<code>  
Gets a property with a given name.   
  
@throws NS_ERROR_FAILURE if a property with that name doesn't exist.  
@throws NS_ERROR_NO_INTERFACE if the found property fails to QI to the   
given iid.  
  
</code>
### set(prop, value) ###
<code>  
Sets a property with a given name to a given value.   
  
</code>
### has(prop) ###
<code>  
Returns true if the property with the given name exists.  
  
</code>
### undefine(prop) ###
<code>  
Undefines a property.  
@throws NS_ERROR_FAILURE if a property with that name doesn't  
already exist.  
  
</code>
### getKeys(count, keys) ###
<code>  
 Returns an array of the keys.  
  
</code>