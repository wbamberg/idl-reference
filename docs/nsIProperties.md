---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIProperties.idl">Source file</a>
</div>

# nsIProperties #

## Methods ##

### get(prop, iid, result) ###
  
Gets a property with a given name.   
  
@throws NS_ERROR_FAILURE if a property with that name doesn't exist.  
@throws NS_ERROR_NO_INTERFACE if the found property fails to QI to the   
given iid.  
  

### set(prop, value) ###
  
Sets a property with a given name to a given value.   
  

### has(prop) ###
  
Returns true if the property with the given name exists.  
  

### undefine(prop) ###
  
Undefines a property.  
@throws NS_ERROR_FAILURE if a property with that name doesn't  
already exist.  
  

### getKeys(count, keys) ###
  
 Returns an array of the keys.  
  
