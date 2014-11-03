---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/tree/nsITreeSelection.idl">Source file</a>
</div>

# nsITreeSelection #

## Methods ##

### isSelected(index) ###
<pre>  
Indicates whether or not the row at the specified index is  
part of the selection.  
  
</pre>
### select(index) ###
<pre>  
Deselect all rows and select the row at the specified index.   
  
</pre>
### timedSelect(index, delay) ###
<pre>  
Perform a timed select.  
  
</pre>
### toggleSelect(index) ###
<pre>  
Toggle the selection state of the row at the specified index.  
  
</pre>
### rangedSelect(startIndex, endIndex, augment) ###
<pre>  
Select the range specified by the indices.  If augment is true,  
then we add the range to the selection without clearing out anything  
else.  If augment is false, everything is cleared except for the specified range.  
  
</pre>
### clearRange(startIndex, endIndex) ###
<pre>  
Clears the range.  
  
</pre>
### clearSelection() ###
<pre>  
Clears the selection.  
  
</pre>
### invertSelection() ###
<pre>  
Inverts the selection.  
  
</pre>
### selectAll() ###
<pre>  
Selects all rows.  
  
</pre>
### getRangeCount() ###
<pre>  
Iterate the selection using these methods.  
  
</pre>
### getRangeAt(i, min, max) ###

### invalidateSelection() ###
<pre>  
Can be used to invalidate the selection.  
  
</pre>
### adjustSelection(index, count) ###
<pre>  
Called when the row count changes to adjust selection indices.  
  
</pre>
## Attributes ##

### tree ###
<pre>  
The tree widget for this selection.  
  
</pre>
### single ###
<pre>  
This attribute is a boolean indicating single selection.  
  
</pre>
### count ###
<pre>  
The number of rows currently selected in this tree.  
  
</pre>
### selectEventsSuppressed ###
<pre>  
This attribute is a boolean indicating whether or not the  
"select" event should fire when the selection is changed using  
one of our methods.  A view can use this to temporarily suppress  
the selection while manipulating all of the indices, e.g., on   
a sort.  
Note: setting this attribute to false will fire a select event.  
  
</pre>
### currentIndex ###
<pre>  
The current item (the one that gets a focus rect in addition to being  
selected).  
  
</pre>
### currentColumn ###
<pre>  
The current column.  
  
</pre>
### shiftSelectPivot ###
<pre>  
The selection "pivot".  This is the first item the user selected as  
part of a ranged select.  
  
</pre>