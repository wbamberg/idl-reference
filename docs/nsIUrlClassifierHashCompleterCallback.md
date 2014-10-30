---
layout: default
---

# nsIUrlClassifierHashCompleterCallback #
  
This interface is implemented by nsIUrlClassifierHashCompleter clients.  
  

## Methods ##

### completion ###
  
A complete hash has been found that matches the partial hash.  
This method may be called 0-n times for a given  
nsIUrlClassifierCompleter::complete() call.  
  
@param hash  
       The 128-bit hash that was discovered.  
@param table  
       The name of the table that this hash belongs to.  
@param chunkId  
       The database chunk that this hash belongs to.  
  

### completionFinished ###
  
The completion is complete.  This method is called once per  
nsIUrlClassifierCompleter::complete() call, after all completion()  
calls are finished.  
  
@param status  
       NS_OK if the request completed successfully, or an error code.  
  
