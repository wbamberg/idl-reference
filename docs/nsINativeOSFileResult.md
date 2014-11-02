---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/osfile/nsINativeOSFileInternals.idl">Source file</a>
</div>
# nsINativeOSFileResult #
  
The result of a successful asynchronous operation.  
  

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
  
