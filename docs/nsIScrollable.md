---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIScrollable.idl">Source file</a>
</div>

# nsIScrollable #
  
The nsIScrollable is an interface that can be implemented by a control that  
supports scrolling.  This is a generic interface without concern for the   
type of content that may be inside.  
  

## Methods ##

### getDefaultScrollbarPreferences(scrollOrientation) ###
  
Get or set the default scrollbar state for all documents in  
this shell.  
  

### setDefaultScrollbarPreferences(scrollOrientation, scrollbarPref) ###

### getScrollbarVisibility(verticalVisible, horizontalVisible) ###
  
Get information about whether the vertical and horizontal scrollbars are  
currently visible.  If you are only interested in one of the visibility  
settings pass nullptr in for the one you aren't interested in.  
  

## Constants ##

### ScrollOrientation_X ###
  
Constants declaring the two scroll orientations a scrollbar can be in.  
ScrollOrientation_X - Horizontal scrolling.  When passing this  
        in to a method you are requesting or setting data for the  
        horizontal scrollbar.  
ScrollOrientation_Y - Vertical scrolling.  When passing this  
        in to a method you are requesting or setting data for the  
        vertical scrollbar.  
  

### ScrollOrientation_Y ###

### Scrollbar_Auto ###
  
Constants declaring the states of the scrollbars.  
ScrollPref_Auto - bars visible only when needed.  
ScrollPref_Never - bars never visible, even when scrolling still possible.  
ScrollPref_Always - bars always visible, even when scrolling is not possible  
  

### Scrollbar_Never ###

### Scrollbar_Always ###
