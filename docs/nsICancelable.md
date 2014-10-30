---
layout: default
---

# nsICancelable #
  
This interface provides a means to cancel an operation that is in progress.  
  

## Methods ##

### cancel(aReason) ###
  
Call this method to request that this object abort whatever operation it  
may be performing.  
  
@param aReason  
       Pass a failure code to indicate the reason why this operation is  
       being canceled.  It is an error to pass a success code.  
  
