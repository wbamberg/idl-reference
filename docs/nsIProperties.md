---
layout: default
---

# nsIProperties #

## get ##

Gets a property with a given name. 

@throws NS_ERROR_FAILURE if a property with that name doesn't exist.
@throws NS_ERROR_NO_INTERFACE if the found property fails to QI to the 
given iid.


## set ##

Sets a property with a given name to a given value. 


## has ##

Returns true if the property with the given name exists.


## undefine ##

Undefines a property.
@throws NS_ERROR_FAILURE if a property with that name doesn't
already exist.


## getKeys ##

 Returns an array of the keys.

