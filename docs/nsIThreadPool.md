---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsIThreadPool.idl">Source file</a>
</div>
# nsIThreadPool #
  
An interface to a thread pool.  A thread pool creates a limited number of  
anonymous (unnamed) worker threads.  An event dispatched to the thread pool  
will be run on the next available worker thread.  
  

## Methods ##

### shutdown() ###
  
Shutdown the thread pool.  This method may not be executed from any thread  
in the thread pool.  Instead, it is meant to be executed from another  
thread (usually the thread that created this thread pool).  When this  
function returns, the thread pool and all of its threads will be shutdown,  
and it will no longer be possible to dispatch tasks to the thread pool.  
  
As a side effect, events on the current thread will be processed.  
  

### setName(aName) ###
  
Set the label for threads in the pool. All threads will be named  
"<aName> #<n>", where <n> is a serial number.  
  

## Attributes ##

### threadLimit ###
  
Get/set the maximum number of threads allowed at one time in this pool.  
  

### idleThreadLimit ###
  
Get/set the maximum number of idle threads kept alive.  
  

### idleThreadTimeout ###
  
Get/set the amount of time in milliseconds before an idle thread is  
destroyed.  
  

### threadStackSize ###
  
Get/set the number of bytes reserved for the stack of all threads in  
the pool. By default this is nsIThreadManager::DEFAULT_STACK_SIZE.  
  

### listener ###
  
An optional listener that will be notified when a thread is created or  
destroyed in the course of the thread pool's operation.  
  
A listener will only receive notifications about threads created after the  
listener is set so it is recommended that the consumer set the listener  
before dispatching the first event. A listener that receives an  
onThreadCreated() notification is guaranteed to always receive the  
corresponding onThreadShuttingDown() notification.  
  
The thread pool takes ownership of the listener and releases it when the  
shutdown() method is called. Threads created after the listener is set will  
also take ownership of the listener so that the listener will be kept alive  
long enough to receive the guaranteed onThreadShuttingDown() notification.  
  
