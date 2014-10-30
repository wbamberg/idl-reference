---
layout: default
---

# nsICancelableRunnable #
  
Represents a task which can be dispatched to a thread for execution and  
which can be cancelled if necessary.  
  

## Methods ##

### cancel ###
  
Cancels a pending task.  If the task has already been executed this will  
be a no-op.  Calling this method twice is considered an error.  
  
@throws NS_ERROR_UNEXPECTED  
  Indicates that the runnable has already been canceled.  
  
