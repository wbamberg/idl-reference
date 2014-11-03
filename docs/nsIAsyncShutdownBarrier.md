---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/asyncshutdown/nsIAsyncShutdown.idl">Source file</a>
</div>

# nsIAsyncShutdownBarrier #
<pre>  
A stage of shutdown that supports blocker registration.  
  
</pre>
## Methods ##

### wait(aOnReady) ###
<pre>  
Wait for all blockers to complete.  
  
Method `aOnReady` will be called once all blockers have finished.  
The callback always receives NS_OK.  
  
</pre>
## Attributes ##

### client ###
<pre>  
The blocker registration capability.  Most services may wish to  
publish this capability to let services that depend on it register  
blockers.  
  
</pre>
### state ###
<pre>  
The state of all the blockers of the barrier.  
  
See the documentation of `nsIAsyncShutdownBlocker` for the  
format.  
  
</pre>