---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/accessible/interfaces/nsIAccessibleSelectable.idl">Source file</a>
</div>

# nsIAccessibleSelectable #
<pre>  
An accessibility interface for selectable widgets.  
  
</pre>
## Methods ##

### getSelectedItemAt(index) ###
<pre>  
Return a nth selected item within the widget.  
  
</pre>
### isItemSelected(index) ###
<pre>  
Return true if the given item is selected.  
  
</pre>
### addItemToSelection(index) ###
<pre>  
Adds the specified item to the widget's selection.  
  
</pre>
### removeItemFromSelection(index) ###
<pre>  
Removes the specified item from the widget's selection.  
  
</pre>
### selectAll() ###
<pre>  
Select all items.  
  
@return false if the object does not accept multiple selection,  
        otherwise true.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>false if the object does not accept multiple selection,  
        otherwise true.  
</td>
</tr>

</table>

### unselectAll() ###
<pre>  
Unselect all items.  
  
</pre>
## Attributes ##

### selectedItems ###
<pre>  
Return an nsIArray of selected items within the widget.  
  
</pre>
### selectedItemCount ###
<pre>  
Return the number of currently selected items.  
  
</pre>