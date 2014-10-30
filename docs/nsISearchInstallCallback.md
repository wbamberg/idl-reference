---
layout: default
---

# nsISearchInstallCallback #

## Methods ##

### onSuccess(engine) ###
  
Called to indicate that the engine addition process succeeded.  
  
@param engine  
       The nsISearchEngine object that was added (will not be null).  
  

### onError(errorCode) ###
  
Called to indicate that the engine addition process failed.  
  
@param errorCode  
       One of the ERROR_* values described above indicating the cause of  
       the failure.  
  

## Constants ##

### ERROR_UNKNOWN_FAILURE ###

### ERROR_DUPLICATE_ENGINE ###
