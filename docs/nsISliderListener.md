---
layout: default
---

# nsISliderListener #

Used for <scale> to listen to slider changes to avoid mutation listeners


## Methods ##

### valueChanged ###

Called when the current, minimum or maximum value has been changed to
newValue. The which parameter will either be 'curpos', 'minpos' or 'maxpos'.
If userChanged is true, then the user changed ths slider, otherwise it
was changed via some other means.


### dragStateChanged ###

Called when the user begins or ends dragging the thumb.

