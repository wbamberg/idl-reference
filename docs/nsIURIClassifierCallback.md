---
layout: default
---

# nsIURIClassifierCallback #
  
Callback function for nsIURIClassifier lookups.  
  

## Methods ##

### onClassifyComplete(aErrorCode) ###
  
Called by the URI classifier service when it is done checking a URI.  
  
Clients are responsible for associating callback objects with classify()  
calls.  
  
@param aErrorCode  
       The error code with which the channel should be cancelled, or  
       NS_OK if the load should continue normally.  
  
