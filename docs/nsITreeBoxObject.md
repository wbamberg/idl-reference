---
layout: default
---

# nsITreeBoxObject #

## Methods ##

### getFirstVisibleRow ###
  
Get the index of the first visible row.  
  

### getLastVisibleRow ###
  
Get the index of the last visible row.  
  

### getPageLength ###
  
Gets the number of possible visible rows.  
  

### ensureRowIsVisible ###
  
Ensures that a row at a given index is visible.  
  

### ensureCellIsVisible ###
  
Ensures that a given cell in the tree is visible.  
  

### scrollToRow ###
  
Scrolls such that the row at index is at the top of the visible view.  
  

### scrollByLines ###
  
Scroll the tree up or down by numLines lines. Positive  
values move down in the tree. Prevents scrolling off the  
end of the tree.   
  

### scrollByPages ###
  
Scroll the tree up or down by numPages pages. A page  
is considered to be the amount displayed by the tree.  
Positive values move down in the tree. Prevents scrolling  
off the end of the tree.  
  

### scrollToCell ###
  
Scrolls such that a given cell is visible (if possible)   
at the top left corner of the visible view.   
  

### scrollToColumn ###
  
Scrolls horizontally so that the specified column is   
at the left of the view (if possible).  
  

### scrollToHorizontalPosition ###
  
Scroll to a specific horizontal pixel position.  
  

### invalidate ###
  
Invalidation methods for fine-grained painting control.  
  

### invalidateColumn ###

### invalidateRow ###

### invalidateCell ###

### invalidateRange ###

### invalidateColumnRange ###

### getRowAt ###
  
A hit test that can tell you what row the mouse is over.  
returns -1 for invalid mouse coordinates.  
  
The coordinate system is the client coordinate system for the  
document this boxObject lives in, and the units are CSS pixels.  
  

### getCellAt ###
  
A hit test that can tell you what cell the mouse is over.  Row is the row index  
hit,  returns -1 for invalid mouse coordinates.  ColID is the column hit.  
ChildElt is the pseudoelement hit: this can have values of  
"cell", "twisty", "image", and "text".  
  
The coordinate system is the client coordinate system for the  
document this boxObject lives in, and the units are CSS pixels.  
  

### getCoordsForCellItem ###
   
Find the coordinates of an element within a specific cell.   
  

### isCellCropped ###
   
Determine if the text of a cell is being cropped or not.  
  

### rowCountChanged ###
  
The view is responsible for calling these notification methods when  
rows are added or removed.  Index is the position at which the new  
rows were added or at which rows were removed.  For  
non-contiguous additions/removals, this method should be called multiple times.  
  

### beginUpdateBatch ###
  
Notify the tree that the view is about to perform a batch  
update, that is, add, remove or invalidate several rows at once.  
This must be followed by calling endUpdateBatch(), otherwise the tree  
will get out of sync.  
  

### endUpdateBatch ###
  
Notify the tree that the view has completed a batch update.  
  

### clearStyleAndImageCaches ###
  
Called on a theme switch to flush out the tree's style and image caches.  
  

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
  
