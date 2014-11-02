---
layout: default
---

# nsIAccessibleSelectable #
  
An accessibility interface for selectable widgets.  
  

## Methods ##

### getSelectedItemAt(index) ###
  
Return a nth selected item within the widget.  
  

### isItemSelected(index) ###
  
Return true if the given item is selected.  
  

### addItemToSelection(index) ###
  
Adds the specified item to the widget's selection.  
  

### removeItemFromSelection(index) ###
  
Removes the specified item from the widget's selection.  
  

### selectAll() ###
  
Select all items.  
  
@return false if the object does not accept multiple selection,  
        otherwise true.  
  

#### Returns ####

<table>

<tr>
<td>false if the object does not accept multiple selection,  
        otherwise true.  
</td>
</tr>

</table>

### unselectAll() ###
  
Unselect all items.  
  

## Attributes ##

### selectedItems ###
  
Return an nsIArray of selected items within the widget.  
  

### selectedItemCount ###
  
Return the number of currently selected items.  
  
