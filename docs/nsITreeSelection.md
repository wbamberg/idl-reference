---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/tree/nsITreeSelection.idl">Source file</a>
</div>

# nsITreeSelection #

## Methods ##

### isSelected(index) ###
<code>  
Indicates whether or not the row at the specified index is  
part of the selection.  
  
</code>
### select(index) ###
<code>  
Deselect all rows and select the row at the specified index.   
  
</code>
### timedSelect(index, delay) ###
<code>  
Perform a timed select.  
  
</code>
### toggleSelect(index) ###
<code>  
Toggle the selection state of the row at the specified index.  
  
</code>
### rangedSelect(startIndex, endIndex, augment) ###
<code>  
Select the range specified by the indices.  If augment is true,  
then we add the range to the selection without clearing out anything  
else.  If augment is false, everything is cleared except for the specified range.  
  
</code>
### clearRange(startIndex, endIndex) ###
<code>  
Clears the range.  
  
</code>
### clearSelection() ###
<code>  
Clears the selection.  
  
</code>
### invertSelection() ###
<code>  
Inverts the selection.  
  
</code>
### selectAll() ###
<code>  
Selects all rows.  
  
</code>
### getRangeCount() ###
<code>  
Iterate the selection using these methods.  
  
</code>
### getRangeAt(i, min, max) ###

### invalidateSelection() ###
<code>  
Can be used to invalidate the selection.  
  
</code>
### adjustSelection(index, count) ###
<code>  
Called when the row count changes to adjust selection indices.  
  
</code>
## Attributes ##

### tree ###
  
The tree widget for this selection.  
  

### single ###
  
This attribute is a boolean indicating single selection.  
  

### count ###
  
The number of rows currently selected in this tree.  
  

### selectEventsSuppressed ###
  
This attribute is a boolean indicating whether or not the  
"select" event should fire when the selection is changed using  
one of our methods.  A view can use this to temporarily suppress  
the selection while manipulating all of the indices, e.g., on   
a sort.  
Note: setting this attribute to false will fire a select event.  
  

### currentIndex ###
  
The current item (the one that gets a focus rect in addition to being  
selected).  
  

### currentColumn ###
  
The current column.  
  

### shiftSelectPivot ###
  
The selection "pivot".  This is the first item the user selected as  
part of a ranged select.  
  
