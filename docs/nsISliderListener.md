---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/nsISliderListener.idl">Source file</a>
</div>

# nsISliderListener #
<code>  
Used for <scale> to listen to slider changes to avoid mutation listeners  
  
</code>
## Methods ##

### valueChanged(which, newValue, userChanged) ###
<code>  
Called when the current, minimum or maximum value has been changed to  
newValue. The which parameter will either be 'curpos', 'minpos' or 'maxpos'.  
If userChanged is true, then the user changed ths slider, otherwise it  
was changed via some other means.  
  
</code>
### dragStateChanged(isDragging) ###
<code>  
Called when the user begins or ends dragging the thumb.  
  
</code>