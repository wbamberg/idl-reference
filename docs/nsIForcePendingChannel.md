---
layout: default
---

# nsIForcePendingChannel #
  
nsIForcePending interface exposes a function that enables overwriting of the normal   
behavior for the channel's IsPending(), forcing 'true' to be returned.  
  

## Methods ##

### forcePending ###
  
forcePending(true) overrides the normal behavior for the   
channel's IsPending(), forcing 'true' to be returned. A call to  
forcePending(false) reverts IsPending() back to normal behavior.  
  
