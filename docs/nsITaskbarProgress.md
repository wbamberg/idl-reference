---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarProgress.idl">Source file</a>
</div>

# nsITaskbarProgress #
<pre>  
Starting in Windows 7, applications can display a progress notification in  
the taskbar. This class wraps around the native functionality to do this.  
  
</pre>
## Methods ##

### setProgressState(state, currentValue, maxValue) ###
<pre>  
Sets the taskbar progress state and value for this window. The currentValue  
and maxValue parameters are optional and should be supplied when |state|  
is one of STATE_NORMAL, STATE_ERROR or STATE_PAUSED.  
  
@throws NS_ERROR_INVALID_ARG if state is STATE_NO_PROGRESS or  
        STATE_INDETERMINATE, and either currentValue or maxValue is not 0.  
@throws NS_ERROR_ILLEGAL_VALUE if currentValue is greater than maxValue.  
  
</pre>
## Constants ##

### STATE_NO_PROGRESS ###
<pre>  
Stop displaying progress on the taskbar button. This should be used when  
the operation is complete or cancelled.  
  
</pre>
### STATE_INDETERMINATE ###
<pre>  
Display a cycling, indeterminate progress bar.  
  
</pre>
### STATE_NORMAL ###
<pre>  
Display a determinate, normal progress bar.  
  
</pre>
### STATE_ERROR ###
<pre>  
Display a determinate, error progress bar.  
  
</pre>
### STATE_PAUSED ###
<pre>  
Display a determinate progress bar indicating that the operation has  
paused.  
  
</pre>