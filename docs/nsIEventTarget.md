---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsIEventTarget.idl">Source file</a>
</div>
# nsIEventTarget #

## Methods ##

### dispatch(event, flags) ###
  
Dispatch an event to this event target.  This function may be called from  
any thread, and it may be called re-entrantly.  
  
@param event  
  The event to dispatch.  
@param flags  
  The flags modifying event dispatch.  The flags are described in detail  
  below.  
  
@throws NS_ERROR_INVALID_ARG  
  Indicates that event is null.  
@throws NS_ERROR_UNEXPECTED  
  Indicates that the thread is shutting down and has finished processing  
events, so this event would never run and has not been dispatched.   
  

#### Parameters ####

<table>

<tr>
<td>event</td>
<td>  The event to dispatch.  
</td>
</tr>

<tr>
<td>flags</td>
<td>  The flags modifying event dispatch.  The flags are described in detail  
  below.  
</td>
</tr>

</table>

### isOnCurrentThread() ###
  
Check to see if this event target is associated with the current thread.  
  
@returns  
  A boolean value that if "true" indicates that events dispatched to this  
  event target will run on the current thread (i.e., the thread calling  
  this method).  
  

#### Returns ####

<table>

<tr>
<td>  A boolean value that if "true" indicates that events dispatched to this  
  event target will run on the current thread (i.e., the thread calling  
  this method).  
</td>
</tr>

</table>

## Constants ##

### DISPATCH_NORMAL ###
  
This flag specifies the default mode of event dispatch, whereby the event  
is simply queued for later processing.  When this flag is specified,  
dispatch returns immediately after the event is queued.  
  

### DISPATCH_SYNC ###
  
This flag specifies the synchronous mode of event dispatch, in which the  
dispatch method does not return until the event has been processed.  
  
NOTE: passing this flag to dispatch may have the side-effect of causing  
other events on the current thread to be processed while waiting for the  
given event to be processed.  
  
