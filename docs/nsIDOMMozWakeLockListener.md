---
layout: default
---

# nsIDOMMozWakeLockListener #

## Methods ##

### callback(aTopic, aState) ###
  
The callback will be called when a lock topic changes its lock  
state.  
  
Possible states are:  
  
 - "unlocked" - nobody holds the wake lock.  
  
 - "locked-foreground" - at least one window holds the wake lock,  
   and it is visible.  
  
 - "locked-background" - at least one window holds the wake lock,  
   but all of them are hidden.  
  
@param aTopic The resource name related to the wake lock.  
@param aState The wake lock state  
  
