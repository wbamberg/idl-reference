---
layout: default
---

# nsIDirectoryService #
  
nsIDirectoryService  
  

## Methods ##

### init() ###
  
init  
  
Must be called. Used internally by XPCOM initialization.  
  
  

### registerProvider(prov) ###
  
registerProvider  
  
Register a provider with the service.  
  
@param prov            The service will keep a strong reference  
                       to this object. It will be released when  
                       the service is released.  
  
  

### unregisterProvider(prov) ###
  
unregisterProvider  
  
Unregister a provider with the service.  
  
@param prov              
  
  
