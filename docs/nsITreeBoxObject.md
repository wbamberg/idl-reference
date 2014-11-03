---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/xul/tree/nsITreeBoxObject.idl">Source file</a>
</div>

# nsITreeBoxObject #

## Methods ##

### getFirstVisibleRow() ###
<code>  
Get the index of the first visible row.  
  
</code>
### getLastVisibleRow() ###
<code>  
Get the index of the last visible row.  
  
</code>
### getPageLength() ###
<code>  
Gets the number of possible visible rows.  
  
</code>
### ensureRowIsVisible(index) ###
<code>  
Ensures that a row at a given index is visible.  
  
</code>
### ensureCellIsVisible(row, col) ###
<code>  
Ensures that a given cell in the tree is visible.  
  
</code>
### scrollToRow(index) ###
<code>  
Scrolls such that the row at index is at the top of the visible view.  
  
</code>
### scrollByLines(numLines) ###
<code>  
Scroll the tree up or down by numLines lines. Positive  
values move down in the tree. Prevents scrolling off the  
end of the tree.   
  
</code>
### scrollByPages(numPages) ###
<code>  
Scroll the tree up or down by numPages pages. A page  
is considered to be the amount displayed by the tree.  
Positive values move down in the tree. Prevents scrolling  
off the end of the tree.  
  
</code>
### scrollToCell(row, col) ###
<code>  
Scrolls such that a given cell is visible (if possible)   
at the top left corner of the visible view.   
  
</code>
### scrollToColumn(col) ###
<code>  
Scrolls horizontally so that the specified column is   
at the left of the view (if possible).  
  
</code>
### scrollToHorizontalPosition(horizontalPosition) ###
<code>  
Scroll to a specific horizontal pixel position.  
  
</code>
### invalidate() ###
<code>  
Invalidation methods for fine-grained painting control.  
  
</code>
### invalidateColumn(col) ###

### invalidateRow(index) ###

### invalidateCell(row, col) ###

### invalidateRange(startIndex, endIndex) ###

### invalidateColumnRange(startIndex, endIndex, col) ###

### getRowAt(x, y) ###
<code>  
A hit test that can tell you what row the mouse is over.  
returns -1 for invalid mouse coordinates.  
  
The coordinate system is the client coordinate system for the  
document this boxObject lives in, and the units are CSS pixels.  
  
</code>
### getCellAt(x, y, row, col, childElt) ###
<code>  
A hit test that can tell you what cell the mouse is over.  Row is the row index  
hit,  returns -1 for invalid mouse coordinates.  ColID is the column hit.  
ChildElt is the pseudoelement hit: this can have values of  
"cell", "twisty", "image", and "text".  
  
The coordinate system is the client coordinate system for the  
document this boxObject lives in, and the units are CSS pixels.  
  
</code>
### getCoordsForCellItem(row, col, element, x, y, width, height) ###
<code>   
Find the coordinates of an element within a specific cell.   
  
</code>
### isCellCropped(row, col) ###
<code>   
Determine if the text of a cell is being cropped or not.  
  
</code>
### rowCountChanged(index, count) ###
<code>  
The view is responsible for calling these notification methods when  
rows are added or removed.  Index is the position at which the new  
rows were added or at which rows were removed.  For  
non-contiguous additions/removals, this method should be called multiple times.  
  
</code>
### beginUpdateBatch() ###
<code>  
Notify the tree that the view is about to perform a batch  
update, that is, add, remove or invalidate several rows at once.  
This must be followed by calling endUpdateBatch(), otherwise the tree  
will get out of sync.  
  
</code>
### endUpdateBatch() ###
<code>  
Notify the tree that the view has completed a batch update.  
  
</code>
### clearStyleAndImageCaches() ###
<code>  
Called on a theme switch to flush out the tree's style and image caches.  
  
</code>
## Attributes ##

### columns ###
  
Obtain the columns.  
  

### view ###
  
The view that backs the tree and that supplies it with its data.  
It is dynamically settable, either using a view attribute on the  
tree tag or by setting this attribute to a new value.  
  

### focused ###
  
Whether or not we are currently focused.  
  

### treeBody ###
  
Obtain the treebody content node  
  

### rowHeight ###
  
Obtain the height of a row.  
  

### rowWidth ###
  
Obtain the width of a row.  
  

### horizontalPosition ###
  
Get the pixel position of the horizontal scrollbar.   
  

### selectionRegion ###
  
Return the region for the visible parts of the selection, in device pixels.  
  
