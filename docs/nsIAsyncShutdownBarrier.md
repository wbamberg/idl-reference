---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/asyncshutdown/nsIAsyncShutdown.idl">Source file</a>
</div>

# nsIAsyncShutdownBarrier #
<code>  
A stage of shutdown that supports blocker registration.  
  
</code>
## Methods ##

### wait(aOnReady) ###
<code>  
Wait for all blockers to complete.  
  
Method `aOnReady` will be called once all blockers have finished.  
The callback always receives NS_OK.  
  
</code>
## Attributes ##

### client ###
  
The blocker registration capability.  Most services may wish to  
publish this capability to let services that depend on it register  
blockers.  
  

### state ###
  
The state of all the blockers of the barrier.  
  
See the documentation of `nsIAsyncShutdownBlocker` for the  
format.  
  
