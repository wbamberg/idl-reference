---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/asyncshutdown/nsIAsyncShutdown.idl">Source file</a>
</div>

# nsIAsyncShutdownBlocker #
<pre>  
A blocker installed by a client to be informed during some stage of  
shutdown and block shutdown asynchronously until some condition is  
complete.  
  
If you wish to use AsyncShutdown, you will need to implement this  
interface (and only this interface).  
  
</pre>
## Methods ##

### blockShutdown(aBarrierClient) ###
<pre>  
Inform the blocker that the stage of shutdown has started.  
Shutdown will NOT proceed until `aBarrierClient.removeBlocker(this)`  
has been called.  
  
</pre>
## Attributes ##

### name ###
<pre>  
The *unique* name of the blocker.  
  
By convention, it should respect the following format:  
"MyModuleName: Doing something while it's time"  
e.g.  
"OS.File: Flushing before profile-before-change"  
  
This attribute is uploaded as part of crash reports.  
  
</pre>
### state ###
<pre>  
The current state of the blocker.  
  
In case of crash, this is converted to JSON and attached to  
the crash report.  
  
This field may be used to provide JSON-style data structures.  
For this purpose, use  
- nsIPropertyBag to represent objects;  
- nsIVariant to represent field values (which may hold nsIPropertyBag  
themselves).  
  
</pre>