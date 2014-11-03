---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xul/templates/nsIXULTemplateBuilder.idl">Source file</a>
</div>

# nsIXULTreeBuilderObserver #
<code>  
nsIXULTreeBuilderObserver  
 This interface allows clients of the XULTreeBuilder to define domain   
 specific handling of specific nsITreeView methods that   
 XULTreeBuilder does not implement.  
  
</code>
## Methods ##

### canDrop(index, orientation, dataTransfer) ###
<code>  
Methods used by the drag feedback code to determine if a drag is allowable at  
the current location. To get the behavior where drops are only allowed on  
items, such as the mailNews folder pane, always return false whe  
the orientation is not DROP_ON.  
  
</code>
### onDrop(row, orientation, dataTransfer) ###
<code>  
Called when the user drops something on this view. The |orientation| param  
specifies before/on/after the given |row|.  
  
</code>
### onToggleOpenState(index) ###
<code>   
Called when an item is opened or closed.   
  
</code>
### onCycleHeader(colID, elt) ###
<code>   
Called when a header is clicked.  
  
</code>
### onCycleCell(row, colID) ###
<code>  
Called when a cell in a non-selectable cycling column (e.g.   
unread/flag/etc.) is clicked.  
  
</code>
### onSelectionChanged() ###
<code>   
Called when selection in the tree changes  
  
</code>
### onPerformAction(action) ###
<code>  
A command API that can be used to invoke commands on the selection.    
The tree will automatically invoke this method when certain keys   
are pressed.  For example, when the DEL key is pressed, performAction   
will be called with the "delete" string.   
  
</code>
### onPerformActionOnRow(action, row) ###
<code>  
A command API that can be used to invoke commands on a specific row.  
  
</code>
### onPerformActionOnCell(action, row, colID) ###
<code>  
A command API that can be used to invoke commands on a specific cell.  
  
</code>
## Constants ##

### DROP_BEFORE ###

### DROP_ON ###

### DROP_AFTER ###
