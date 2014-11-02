---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsIThreadPool.idl">Source file</a>
</div>
# nsIThreadPoolListener #

## Methods ##

### onThreadCreated() ###
  
Called when a new thread is created by the thread pool. The notification  
happens on the newly-created thread.  
  

### onThreadShuttingDown() ###
  
Called when a thread is about to be destroyed by the thread pool. The  
notification happens on the thread that is about to be destroyed.  
  
