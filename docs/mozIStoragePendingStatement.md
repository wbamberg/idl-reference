---
layout: default
---

# mozIStoragePendingStatement #

## Methods ##

### cancel() ###
  
Cancels a pending statement, if possible.  This will only fail if you try  
cancel more than once.  
  
@note For read statements (such as SELECT), you will no longer receive any  
      notifications about results once cancel is called.  
  
