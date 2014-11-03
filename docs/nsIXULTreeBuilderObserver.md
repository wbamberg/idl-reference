---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xul/templates/nsIXULTemplateBuilder.idl">Source file</a>
</div>

# nsIXULTreeBuilderObserver #
  
nsIXULTreeBuilderObserver  
 This interface allows clients of the XULTreeBuilder to define domain   
 specific handling of specific nsITreeView methods that   
 XULTreeBuilder does not implement.  
  

## Methods ##

### canDrop(index, orientation, dataTransfer) ###
  
Methods used by the drag feedback code to determine if a drag is allowable at  
the current location. To get the behavior where drops are only allowed on  
items, such as the mailNews folder pane, always return false whe  
the orientation is not DROP_ON.  
  

### onDrop(row, orientation, dataTransfer) ###
  
Called when the user drops something on this view. The |orientation| param  
specifies before/on/after the given |row|.  
  

### onToggleOpenState(index) ###
   
Called when an item is opened or closed.   
  

### onCycleHeader(colID, elt) ###
   
Called when a header is clicked.  
  

### onCycleCell(row, colID) ###
  
Called when a cell in a non-selectable cycling column (e.g.   
unread/flag/etc.) is clicked.  
  

### onSelectionChanged() ###
   
Called when selection in the tree changes  
  

### onPerformAction(action) ###
  
A command API that can be used to invoke commands on the selection.    
The tree will automatically invoke this method when certain keys   
are pressed.  For example, when the DEL key is pressed, performAction   
will be called with the "delete" string.   
  

### onPerformActionOnRow(action, row) ###
  
A command API that can be used to invoke commands on a specific row.  
  

### onPerformActionOnCell(action, row, colID) ###
  
A command API that can be used to invoke commands on a specific cell.  
  

## Constants ##

### DROP_BEFORE ###

### DROP_ON ###

### DROP_AFTER ###
