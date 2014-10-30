---
layout: default
---

# nsIThreadObserver #
  
This interface provides the observer with hooks to implement a layered  
event queue.  For example, it is possible to overlay processing events  
for a GUI toolkit on top of the events for a thread:  
  
  var NativeQueue;  
  Observer = {  
    onDispatchedEvent(thread) {  
      NativeQueue.signal();  
    }  
    onProcessNextEvent(thread, mayWait, recursionDepth) {  
      if (NativeQueue.hasNextEvent())  
        NativeQueue.processNextEvent();  
      while (mayWait && !thread.hasPendingEvent()) {  
        NativeQueue.wait();  
        NativeQueue.processNextEvent();  
      }  
    }  
  };  
  
NOTE: The implementation of this interface must be threadsafe.  
  
NOTE: It is valid to change the thread's observer during a call to an  
      observer method.  
  
NOTE: Will be split into two interfaces soon: one for onProcessNextEvent and  
      afterProcessNextEvent, then another that inherits the first and adds  
      onDispatchedEvent.  
  

## Methods ##

### onDispatchedEvent(thread) ###
  
This method is called after an event has been dispatched to the thread.  
This method may be called from any thread.   
  
@param thread  
  The thread where the event is being dispatched.  
  

### onProcessNextEvent(thread, mayWait, recursionDepth) ###
  
This method is called when nsIThread::ProcessNextEvent is called.  It does  
not guarantee that an event is actually going to be processed.  This method  
is only called on the target thread.  
  
@param thread  
  The thread being asked to process another event.  
@param mayWait  
  Indicates whether or not the method is allowed to block the calling  
  thread.  For example, this parameter is false during thread shutdown.  
@param recursionDepth  
  Indicates the number of calls to ProcessNextEvent on the call stack in  
  addition to the current call.  
  

### afterProcessNextEvent(thread, recursionDepth, eventWasProcessed) ###
  
This method is called (from nsIThread::ProcessNextEvent) after an event  
is processed.  It does not guarantee that an event was actually processed  
(depends on the value of |eventWasProcessed|.  This method is only called  
on the target thread.  
  
@param thread  
  The thread that processed another event.  
@param recursionDepth  
  Indicates the number of calls to ProcessNextEvent on the call stack in  
  addition to the current call.  
@param eventWasProcessed  
  Indicates whether an event was actually processed. May be false if the  
  |mayWait| flag was false when calling nsIThread::ProcessNextEvent().  
  
