---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xul/templates/nsIXULTemplateBuilder.idl">Source file</a>
</div>

# nsIXULTreeBuilderObserver #
<pre>  
nsIXULTreeBuilderObserver  
 This interface allows clients of the XULTreeBuilder to define domain   
 specific handling of specific nsITreeView methods that   
 XULTreeBuilder does not implement.  
  
</pre>
## Methods ##

### canDrop(index, orientation, dataTransfer) ###
<pre>  
Methods used by the drag feedback code to determine if a drag is allowable at  
the current location. To get the behavior where drops are only allowed on  
items, such as the mailNews folder pane, always return false whe  
the orientation is not DROP_ON.  
  
</pre>
### onDrop(row, orientation, dataTransfer) ###
<pre>  
Called when the user drops something on this view. The |orientation| param  
specifies before/on/after the given |row|.  
  
</pre>
### onToggleOpenState(index) ###
<pre>   
Called when an item is opened or closed.   
  
</pre>
### onCycleHeader(colID, elt) ###
<pre>   
Called when a header is clicked.  
  
</pre>
### onCycleCell(row, colID) ###
<pre>  
Called when a cell in a non-selectable cycling column (e.g.   
unread/flag/etc.) is clicked.  
  
</pre>
### onSelectionChanged() ###
<pre>   
Called when selection in the tree changes  
  
</pre>
### onPerformAction(action) ###
<pre>  
A command API that can be used to invoke commands on the selection.    
The tree will automatically invoke this method when certain keys   
are pressed.  For example, when the DEL key is pressed, performAction   
will be called with the "delete" string.   
  
</pre>
### onPerformActionOnRow(action, row) ###
<pre>  
A command API that can be used to invoke commands on a specific row.  
  
</pre>
### onPerformActionOnCell(action, row, colID) ###
<pre>  
A command API that can be used to invoke commands on a specific cell.  
  
</pre>
## Constants ##

### DROP_BEFORE ###

### DROP_ON ###

### DROP_AFTER ###
