---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleSelectable.idl">Source file</a>
</div>

# nsIAccessibleSelectable #
<code>  
An accessibility interface for selectable widgets.  
  
</code>
## Methods ##

### getSelectedItemAt(index) ###
<code>  
Return a nth selected item within the widget.  
  
</code>
### isItemSelected(index) ###
<code>  
Return true if the given item is selected.  
  
</code>
### addItemToSelection(index) ###
<code>  
Adds the specified item to the widget's selection.  
  
</code>
### removeItemFromSelection(index) ###
<code>  
Removes the specified item from the widget's selection.  
  
</code>
### selectAll() ###
<code>  
Select all items.  
  
@return false if the object does not accept multiple selection,  
        otherwise true.  
  
</code>
#### Returns ####

<table>

<tr>
<td>false if the object does not accept multiple selection,  
        otherwise true.  
</td>
</tr>

</table>

### unselectAll() ###
<code>  
Unselect all items.  
  
</code>
## Attributes ##

### selectedItems ###
  
Return an nsIArray of selected items within the widget.  
  

### selectedItemCount ###
  
Return the number of currently selected items.  
  
