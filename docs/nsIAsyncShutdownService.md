---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/asyncshutdown/nsIAsyncShutdown.idl">Source file</a>
</div>

# nsIAsyncShutdownService #
<pre>  
A service that allows registering shutdown-time dependencies.  
  
</pre>
## Methods ##

### makeBarrier(aName) ###
<pre>  
Create a new barrier.  
  
By convention, the name should respect the following format:  
"MyModuleName: Doing something while it's time"  
e.g.  
"OS.File: Waiting for clients to flush before shutting down"  
  
This attribute is uploaded as part of crash reports.  
  
</pre>
## Attributes ##

### profileBeforeChange ###
<pre>  
Barrier for notification profile-before-change.  
  
</pre>
### profileChangeTeardown ###
<pre>  
Barrier for notification profile-change-teardown.  
  
</pre>
### sendTelemetry ###
<pre>  
Barrier for notification profile-before-change2.  
  
</pre>
### webWorkersShutdown ###
<pre>  
Barrier for notification web-workers-shutdown.  
  
</pre>
### xpcomThreadsShutdown ###
<pre>  
Barrier for notification xpcom-threads-shutdown.  
  
</pre>