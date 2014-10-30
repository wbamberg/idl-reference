---
layout: default
---

# nsIXULTreeBuilderObserver #
  
nsIXULTreeBuilderObserver  
 This interface allows clients of the XULTreeBuilder to define domain   
 specific handling of specific nsITreeView methods that   
 XULTreeBuilder does not implement.  
  

## Methods ##

### canDrop ###
  
Methods used by the drag feedback code to determine if a drag is allowable at  
the current location. To get the behavior where drops are only allowed on  
items, such as the mailNews folder pane, always return false whe  
the orientation is not DROP_ON.  
  

### onDrop ###
  
Called when the user drops something on this view. The |orientation| param  
specifies before/on/after the given |row|.  
  

### onToggleOpenState ###
   
Called when an item is opened or closed.   
  

### onCycleHeader ###
   
Called when a header is clicked.  
  

### onCycleCell ###
  
Called when a cell in a non-selectable cycling column (e.g.   
unread/flag/etc.) is clicked.  
  

### onSelectionChanged ###
   
Called when selection in the tree changes  
  

### onPerformAction ###
  
A command API that can be used to invoke commands on the selection.    
The tree will automatically invoke this method when certain keys   
are pressed.  For example, when the DEL key is pressed, performAction   
will be called with the "delete" string.   
  

### onPerformActionOnRow ###
  
A command API that can be used to invoke commands on a specific row.  
  

### onPerformActionOnCell ###
  
A command API that can be used to invoke commands on a specific cell.  
  

## Constants ##

### DROP_BEFORE ###

### DROP_ON ###

### DROP_AFTER ###
