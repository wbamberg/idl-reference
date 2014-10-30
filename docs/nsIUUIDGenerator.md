---
layout: default
---

# nsIUUIDGenerator #
  
nsIUUIDGenerator is implemented by a service that can generate  
universally unique identifiers, ideally using any platform-native  
method for generating UUIDs.  
  

## Methods ##

### generateUUID ###
  
Obtains a new UUID using appropriate platform-specific methods to  
obtain a nsID that can be considered to be globally unique.  
  
@returns an nsID filled in with a new UUID.  
  
@throws NS_ERROR_FAILURE if a UUID cannot be generated (e.g. if  
an underlying source of randomness is not available)  
  

### generateUUIDInPlace ###
  
Obtain a new UUID like the generateUUID method, but place it in  
the provided nsID pointer instead of allocating a new nsID.  
  
@param id an existing nsID pointer where the UUID will be stored.  
  
@throws NS_ERROR_FAILURE if a UUID cannot be generated (e.g. if  
an underlying source of randomness is not available)  
  
