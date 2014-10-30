---
layout: default
---

# nsIDNSListener #
  
nsIDNSListener  
  

## Methods ##

### onLookupComplete ###
  
called when an asynchronous host lookup completes.  
  
@param aRequest  
       the value returned from asyncResolve.  
@param aRecord  
       the DNS record corresponding to the hostname that was resolved.  
       this parameter is null if there was an error.  
@param aStatus  
       if the lookup failed, this parameter gives the reason.  
  
