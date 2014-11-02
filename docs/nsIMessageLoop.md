---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIMessageLoop.idl">Source file</a>
</div>
# nsIMessageLoop #
  
This service allows access to the current thread's Chromium MessageLoop  
instance, with some extra sugar added.  If you're calling from C++, it may  
or may not make sense for you to use this interface.  If you're calling from  
JS, you don't have a choice!  
  
Right now, you can only call PostIdleTask(), but nothing is stopping you  
from adding other methods.  
  
nsIMessageLoop's contractid is "@mozilla.org/message-loop;1".  
  

## Methods ##

### postIdleTask(task, ensureRunsAfterMS) ###
  
Posts a task to be run when this thread's message loop is idle, or after  
ensureRunsAfterMS milliseconds have elapsed.  (That is, the task is  
guaranteed to run /eventually/.)  
  
Note that if the event loop is busy, we will hold a reference to the task  
until ensureRunsAfterMS milliseconds have elapsed.  Be careful when  
specifying long timeouts and tasks which hold references to windows or  
other large objects, because you can leak memory in a difficult-to-detect  
way!  
  
