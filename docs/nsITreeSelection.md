---
layout: default
---

# nsITreeSelection #

## Methods ##

### isSelected ###

Indicates whether or not the row at the specified index is
part of the selection.


### select ###

Deselect all rows and select the row at the specified index. 


### timedSelect ###

Perform a timed select.


### toggleSelect ###

Toggle the selection state of the row at the specified index.


### rangedSelect ###

Select the range specified by the indices.  If augment is true,
then we add the range to the selection without clearing out anything
else.  If augment is false, everything is cleared except for the specified range.


### clearRange ###

Clears the range.


### clearSelection ###

Clears the selection.


### invertSelection ###

Inverts the selection.


### selectAll ###

Selects all rows.


### getRangeCount ###

Iterate the selection using these methods.


### getRangeAt ###

### invalidateSelection ###

Can be used to invalidate the selection.


### adjustSelection ###

Called when the row count changes to adjust selection indices.


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

