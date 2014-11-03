---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIScrollable.idl">Source file</a>
</div>

# nsIScrollable #
<pre>  
The nsIScrollable is an interface that can be implemented by a control that  
supports scrolling.  This is a generic interface without concern for the   
type of content that may be inside.  
  
</pre>
## Methods ##

### getDefaultScrollbarPreferences(scrollOrientation) ###
<pre>  
Get or set the default scrollbar state for all documents in  
this shell.  
  
</pre>
### setDefaultScrollbarPreferences(scrollOrientation, scrollbarPref) ###

### getScrollbarVisibility(verticalVisible, horizontalVisible) ###
<pre>  
Get information about whether the vertical and horizontal scrollbars are  
currently visible.  If you are only interested in one of the visibility  
settings pass nullptr in for the one you aren't interested in.  
  
</pre>
## Constants ##

### ScrollOrientation_X ###
<pre>  
Constants declaring the two scroll orientations a scrollbar can be in.  
ScrollOrientation_X - Horizontal scrolling.  When passing this  
        in to a method you are requesting or setting data for the  
        horizontal scrollbar.  
ScrollOrientation_Y - Vertical scrolling.  When passing this  
        in to a method you are requesting or setting data for the  
        vertical scrollbar.  
  
</pre>
### ScrollOrientation_Y ###

### Scrollbar_Auto ###
<pre>  
Constants declaring the states of the scrollbars.  
ScrollPref_Auto - bars visible only when needed.  
ScrollPref_Never - bars never visible, even when scrolling still possible.  
ScrollPref_Always - bars always visible, even when scrolling is not possible  
  
</pre>
### Scrollbar_Never ###

### Scrollbar_Always ###
