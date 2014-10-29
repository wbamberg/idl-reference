---
layout: default
---

# nsIDirectoryService #

nsIDirectoryService


## init ##

init

Must be called. Used internally by XPCOM initialization.



## registerProvider ##

registerProvider

Register a provider with the service.

@param prov            The service will keep a strong reference
                       to this object. It will be released when
                       the service is released.



## unregisterProvider ##

unregisterProvider

Unregister a provider with the service.

@param prov            


