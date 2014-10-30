---
layout: default
---

# nsIAccessibleSelectable #
  
An accessibility interface for selectable widgets.  
  

## Methods ##

### getSelectedItemAt ###
  
Return a nth selected item within the widget.  
  

### isItemSelected ###
  
Return true if the given item is selected.  
  

### addItemToSelection ###
  
Adds the specified item to the widget's selection.  
  

### removeItemFromSelection ###
  
Removes the specified item from the widget's selection.  
  

### selectAll ###
  
Select all items.  
  
@return false if the object does not accept multiple selection,  
        otherwise true.  
  

### unselectAll ###
  
Unselect all items.  
  

## Attributes ##

### selectedItems ###
  
Return an nsIArray of selected items within the widget.  
  

### selectedItemCount ###
  
Return the number of currently selected items.  
  
