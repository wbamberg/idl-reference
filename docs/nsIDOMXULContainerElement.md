---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/xul/nsIDOMXULContainerElement.idl">Source file</a>
</div>

# nsIDOMXULContainerElement #

## Methods ##

### appendItem(aLabel, aValue) ###
  
Creates an item for the given label and value and appends it to the  
container.  
  
@param aLabel - the label for the new item  
@param aValue - the value of the new item  
  

#### Parameters ####

<table>

<tr>
<td>aLabel</td>
<td>- the label for the new item  
</td>
</tr>

<tr>
<td>aValue</td>
<td>- the value of the new item  
</td>
</tr>

</table>

### insertItemAt(aIndex, aLabel, aValue) ###
  
Creates an item for the given label and value and inserts it into the  
container at the specified position.  
  
@param aIndex - the index where the new item will be inserted  
@param aLabel - the label for the new item  
@param aValue - the value of the new item  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>- the index where the new item will be inserted  
</td>
</tr>

<tr>
<td>aLabel</td>
<td>- the label for the new item  
</td>
</tr>

<tr>
<td>aValue</td>
<td>- the value of the new item  
</td>
</tr>

</table>

### removeItemAt(aIndex) ###
  
Removes an item from the container.  
  
@param aIndex - index of the item to remove  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>- index of the item to remove  
</td>
</tr>

</table>

### getIndexOfItem(aItem) ###
  
Returns the index of an item or -1 if the item is not in the container.  
  
@param aItem - the item to determine the index of  
  

#### Parameters ####

<table>

<tr>
<td>aItem</td>
<td>- the item to determine the index of  
</td>
</tr>

</table>

### getItemAtIndex(aIndex) ###
  
Returns the item at a given index or null if the item is not is the  
container.  
  
@param aIndex - the index of the item to return  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>- the index of the item to return  
</td>
</tr>

</table>

## Attributes ##

### itemCount ###
  
Returns a count of items in the container.  
  
