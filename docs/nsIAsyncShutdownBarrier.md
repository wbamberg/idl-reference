---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/asyncshutdown/nsIAsyncShutdown.idl">Source file</a>
</div>
# nsIAsyncShutdownBarrier #
  
A stage of shutdown that supports blocker registration.  
  

## Methods ##

### wait(aOnReady) ###
  
Wait for all blockers to complete.  
  
Method `aOnReady` will be called once all blockers have finished.  
The callback always receives NS_OK.  
  

## Attributes ##

### client ###
  
The blocker registration capability.  Most services may wish to  
publish this capability to let services that depend on it register  
blockers.  
  

### state ###
  
The state of all the blockers of the barrier.  
  
See the documentation of `nsIAsyncShutdownBlocker` for the  
format.  
  
