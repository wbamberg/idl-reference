---
layout: default
---

# mozILivemarkCallback #

## Methods ##

### onCompletion(aStatus, aLivemark) ###
  
Invoked when a livemark is added, removed or retrieved.  
  
@param aStatus  
       Whether the request was completed successfully.  
       Use Components.isSuccessCode(aStatus) to check this.  
@param aLivemark  
       A mozILivemark object representing the livemark, or null on removal.  
  
