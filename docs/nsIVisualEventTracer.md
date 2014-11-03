---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIVisualEventTracer.idl">Source file</a>
</div>

# nsIVisualEventTracer #
  
Interface to control the visual event tracer feature.  The result  
is a log of various events that are monitored by a custom code  
instrumentation around the mozilla code base.  
  

## Methods ##

### start(minBacklogSeconds) ###
  
Start the logging now.  No affect if already started.  
Current backlog is deleted by this call otherwise.  
  
  

#### Parameters ####

<table>

<tr>
<td>minBacklogSeconds</td>
<td>   Manimum time to keep the backlog.  Entries of the log are discarded  
   when their age is more then value of this argument.  
</td>
</tr>

</table>

### stop() ###
  
Stop the logging now.  Backlog is kept in memory.  
  

### snapshot() ###
  
Obtain the log.  This can be called whenever you want.  
  
  

#### Returns ####

<table>

<tr>
<td>   Result is an object that keeps snaphot of the log from  
   time this method has been called.  You can then access  
   the log using the object.  Calling stop() on the tracer  
   doesn't delete this log.  
</td>
</tr>

</table>
