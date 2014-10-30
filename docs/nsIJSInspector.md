---
layout: default
---

# nsIJSInspector #
  
Utilities for running nested event loops, asking them to return, and  
keeping track of which ones are still running.  
  

## Methods ##

### enterNestedEventLoop ###
  
Process the current thread's event queue, calling event handlers until  
a call to exitNestedEventLoop, below, asks us to return.  
  
The name 'enterNestedEventLoop' may be misleading if read too literally.  
This method loops calling event handlers until one asks it to stop, and  
then returns. So by that point, the nested event loop has been not only  
entered, but also run and exited.  
  
When enterNestedEventLoop calls an event handler, that handler may itself  
call enterNestedEventLoop, and so on, so that there may be arbitrarily  
many such calls on the stack at the same time.  
  
We say an enterNestedEventLoop call is "running" if it has not yet been  
asked to return, or "stopped" if it has been asked to return once it has  
finished processing the current event.  
  
@param requestor   A token of the caller's choice to identify this event  
                   loop.  
  
@return depth      The number of running enterNestedEventLoop calls  
                   remaining, now that this one has returned.  
  
                   (Note that not all calls still on the stack are  
                   necessary running; exitNestedEventLoop can ask any  
                   number of enterNestedEventLoop calls to return.)  
  

### exitNestedEventLoop ###
  
Stop the youngest running enterNestedEventLoop call, asking it to return  
once it has finished processing the current event.  
  
The name 'exitNestedEventLoop' may be misleading if read too literally.  
The affected event loop does not return immediately when this method is  
called. Rather, this method simply returns to its caller; the affected  
loop's current event handler is allowed to run to completion; and then  
that loop returns without processing any more events.  
  
This method ignores loops that have already been stopped, and operates on  
the youngest loop that is still running. Each call to this method stops  
another running loop.  
  
@return depth      The number of running enterNestedEventLoop calls  
                   remaining, now that one has been stopped.  
  
@throws NS_ERROR_FAILURE if there are no running enterNestedEventLoop calls.  
  

## Attributes ##

### eventLoopNestLevel ###
  
The number of running enterNestedEventLoop calls on the stack.  
This count does not include stopped enterNestedEventLoop calls.  
  

### lastNestRequestor ###
  
The |requestor| value that was passed to the youngest running  
enterNestedEventLoop call.  
  
