---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/tree/nsITreeView.idl">Source file</a>
</div>

# nsITreeView #

## Methods ##

### getRowProperties(index) ###
<pre>   
A whitespace delimited list of properties.  For each property X the view  
gives back will cause the pseudoclasses  ::-moz-tree-cell(x),  
::-moz-tree-row(x), ::-moz-tree-twisty(x), ::-moz-tree-image(x),  
::-moz-tree-cell-text(x).  to be matched on the pseudoelement  
::moz-tree-row.  
  
</pre>
### getCellProperties(row, col) ###
<pre>  
A whitespace delimited list of properties for a given cell.  Each  
property, x, that the view gives back will cause the pseudoclasses  
 ::-moz-tree-cell(x), ::-moz-tree-row(x), ::-moz-tree-twisty(x),  
 ::-moz-tree-image(x), ::-moz-tree-cell-text(x). to be matched on the  
 cell.  
  
</pre>
### getColumnProperties(col) ###
<pre>  
Called to get properties to paint a column background.  For shading the sort  
column, etc.  
  
</pre>
### isContainer(index) ###
<pre>  
Methods that can be used to test whether or not a twisty should be drawn,  
and if so, whether an open or closed twisty should be used.  
  
</pre>
### isContainerOpen(index) ###

### isContainerEmpty(index) ###

### isSeparator(index) ###
<pre>  
isSeparator is used to determine if the row at index is a separator.  
A value of true will result in the tree drawing a horizontal separator.  
The tree uses the ::moz-tree-separator pseudoclass to draw the separator.  
  
</pre>
### isSorted() ###
<pre>  
Specifies if there is currently a sort on any column. Used mostly by dragdrop  
to affect drop feedback.  
  
</pre>
### canDrop(index, orientation, dataTransfer) ###
<pre>  
Methods used by the drag feedback code to determine if a drag is allowable at  
the current location. To get the behavior where drops are only allowed on  
items, such as the mailNews folder pane, always return false when  
the orientation is not DROP_ON.  
  
</pre>
### drop(row, orientation, dataTransfer) ###
<pre>  
Called when the user drops something on this view. The |orientation| param  
specifies before/on/after the given |row|.  
  
</pre>
### getParentIndex(rowIndex) ###
<pre>  
Methods used by the tree to draw thread lines in the tree.  
getParentIndex is used to obtain the index of a parent row.  
If there is no parent row, getParentIndex returns -1.  
  
</pre>
### hasNextSibling(rowIndex, afterIndex) ###
<pre>  
hasNextSibling is used to determine if the row at rowIndex has a nextSibling  
that occurs *after* the index specified by afterIndex.  Code that is forced  
to march down the view looking at levels can optimize the march by starting  
at afterIndex+1.  
  
</pre>
### getLevel(index) ###
<pre>  
The level is an integer value that represents  
the level of indentation.  It is multiplied by the width specified in the   
:moz-tree-indentation pseudoelement to compute the exact indendation.  
  
</pre>
### getImageSrc(row, col) ###
<pre>  
The image path for a given cell. For defining an icon for a cell.  
If the empty string is returned, the :moz-tree-image pseudoelement  
will be used.  
  
</pre>
### getProgressMode(row, col) ###

### getCellValue(row, col) ###
<pre>  
The value for a given cell. This method is only called for columns  
of type other than |text|.  
  
</pre>
### getCellText(row, col) ###
<pre>  
The text for a given cell.  If a column consists only of an image, then  
the empty string is returned.    
  
</pre>
### setTree(tree) ###
<pre>  
Called during initialization to link the view to the front end box object.  
  
</pre>
### toggleOpenState(index) ###
<pre>  
Called on the view when an item is opened or closed.  
  
</pre>
### cycleHeader(col) ###
<pre>  
Called on the view when a header is clicked.  
  
</pre>
### selectionChanged() ###
<pre>  
Should be called from a XUL onselect handler whenever the selection changes.  
  
</pre>
### cycleCell(row, col) ###
<pre>  
Called on the view when a cell in a non-selectable cycling column (e.g., unread/flag/etc.) is clicked.  
  
</pre>
### isEditable(row, col) ###
<pre>  
isEditable is called to ask the view if the cell contents are editable.  
A value of true will result in the tree popping up a text field when   
the user tries to inline edit the cell.  
  
</pre>
### isSelectable(row, col) ###
<pre>  
isSelectable is called to ask the view if the cell is selectable.  
This method is only called if the selection style is |cell| or |text|.  
XXXvarga shouldn't this be called isCellSelectable?  
  
</pre>
### setCellValue(row, col, value) ###
<pre>  
setCellValue is called when the value of the cell has been set by the user.  
This method is only called for columns of type other than |text|.  
  
</pre>
### setCellText(row, col, value) ###
<pre>  
setCellText is called when the contents of the cell have been edited by the user.  
  
</pre>
### performAction(action) ###
<pre>  
A command API that can be used to invoke commands on the selection.  The tree  
will automatically invoke this method when certain keys are pressed.  For example,  
when the DEL key is pressed, performAction will be called with the "delete" string.  
  
</pre>
### performActionOnRow(action, row) ###
<pre>  
A command API that can be used to invoke commands on a specific row.  
  
</pre>
### performActionOnCell(action, row, col) ###
<pre>  
A command API that can be used to invoke commands on a specific cell.  
  
</pre>
## Attributes ##

### rowCount ###
<pre>  
The total number of rows in the tree (including the offscreen rows).  
  
</pre>
### selection ###
<pre>  
The selection for this view.  
  
</pre>
## Constants ##

### DROP_BEFORE ###

### DROP_ON ###

### DROP_AFTER ###

### PROGRESS_NORMAL ###
<pre>  
The progress mode for a given cell. This method is only called for  
columns of type |progressmeter|.  
  
</pre>
### PROGRESS_UNDETERMINED ###

### PROGRESS_NONE ###
