---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/osfile/nsINativeOSFileInternals.idl">Source file</a>
</div>

# nsINativeOSFileResult #
<code>  
The result of a successful asynchronous operation.  
  
</code>
## Attributes ##

### result ###
  
The actual value produced by the operation.  
  
Actual type of this value depends on the options passed to the  
operation.  
  

### dispatchDurationMS ###
  
Delay between when the operation was requested on the main thread and  
when the operation was started off main thread.  
  

### executionDurationMS ###
  
Duration of the off main thread execution.  
  
