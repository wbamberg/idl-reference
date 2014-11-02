---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarProgress.idl">Source file</a>
</div>
# nsITaskbarProgress #
  
Starting in Windows 7, applications can display a progress notification in  
the taskbar. This class wraps around the native functionality to do this.  
  

## Methods ##

### setProgressState(state, currentValue, maxValue) ###
  
Sets the taskbar progress state and value for this window. The currentValue  
and maxValue parameters are optional and should be supplied when |state|  
is one of STATE_NORMAL, STATE_ERROR or STATE_PAUSED.  
  
@throws NS_ERROR_INVALID_ARG if state is STATE_NO_PROGRESS or  
        STATE_INDETERMINATE, and either currentValue or maxValue is not 0.  
@throws NS_ERROR_ILLEGAL_VALUE if currentValue is greater than maxValue.  
  

## Constants ##

### STATE_NO_PROGRESS ###
  
Stop displaying progress on the taskbar button. This should be used when  
the operation is complete or cancelled.  
  

### STATE_INDETERMINATE ###
  
Display a cycling, indeterminate progress bar.  
  

### STATE_NORMAL ###
  
Display a determinate, normal progress bar.  
  

### STATE_ERROR ###
  
Display a determinate, error progress bar.  
  

### STATE_PAUSED ###
  
Display a determinate progress bar indicating that the operation has  
paused.  
  
