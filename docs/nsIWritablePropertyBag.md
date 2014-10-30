---
layout: default
---

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
  
