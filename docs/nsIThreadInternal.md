---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsIThreadInternal.idl">Source file</a>
</div>

# nsIThreadInternal #
  
The XPCOM thread object implements this interface, which allows a consumer  
to observe dispatch activity on the thread.  
  

## Methods ##

### addObserver(observer) ###
  
Add an observer that will *only* receive onProcessNextEvent,  
beforeProcessNextEvent. and afterProcessNextEvent callbacks. Always called  
on the target thread, and the implementation does not have to be  
threadsafe. Order of callbacks is not guaranteed (i.e.  
afterProcessNextEvent may be called first depending on whether or not the  
observer is added in a nested loop). Holds a strong ref.  
  

### removeObserver(observer) ###
  
Remove an observer added via the addObserver call. Once removed the  
observer will never be called again by the thread.  
  

### pushEventQueue() ###
  
This method causes any events currently enqueued on the thread to be  
suppressed until PopEventQueue is called, and any event dispatched to this  
thread's nsIEventTarget will queue as well. Calls to PushEventQueue may be  
nested and must each be paired with a call to PopEventQueue in order to  
restore the original state of the thread. The returned nsIEventTarget may  
be used to push events onto the nested queue. Dispatching will be disabled  
once the event queue is popped. The thread will only ever process pending  
events for the innermost event queue. Must only be called on the target  
thread.  
  

### popEventQueue(aInnermostTarget) ###
  
Revert a call to PushEventQueue. When an event queue is popped, any events  
remaining in the queue are appended to the elder queue. This also causes  
the nsIEventTarget returned from PushEventQueue to stop dispatching events.  
Must only be called on the target thread, and with the innermost event  
queue.  
  

## Attributes ##

### observer ###
  
Get/set the current thread observer (may be null).  This attribute may be  
read from any thread, but must only be set on the thread corresponding to  
this thread object.  The observer will be released on the thread  
corresponding to this thread object after all other events have been  
processed during a call to Shutdown.  
  

### recursionDepth ###
  
The current recursion depth, 0 when no events are running, 1 when a single  
event is running, and higher when nested events are running. Must only be  
called on the target thread.  
  
