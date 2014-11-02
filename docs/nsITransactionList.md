---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/txmgr/nsITransactionList.idl">Source file</a>
</div>

# nsITransactionList #

## Methods ##

### itemIsBatch(aIndex) ###
  
itemIsBatch() returns true if the item at aIndex is a batch. Note that  
currently there is no requirement for a TransactionManager implementation  
to associate a toplevel nsITransaction with a batch so it is possible for  
itemIsBatch() to return true and getItem() to return null. However, you  
can still access the transactions contained in the batch with a call to  
getChildListForItem().  
@param aIndex The index of the item in the list.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>The index of the item in the list.  
</td>
</tr>

</table>

### getItem(aIndex) ###
  
getItem() returns the transaction at the given index in the list. Note that  
a null can be returned here if the item is a batch. The transaction  
returned is AddRef'd so it is up to the caller to Release the transaction  
when it is done.  
@param aIndex The index of the item in the list.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>The index of the item in the list.  
</td>
</tr>

</table>

### getData(aIndex, aLength, aData) ###
  
getData() returns the data (of type nsISupports array) associated with  
the transaction list.  
  

### getNumChildrenForItem(aIndex) ###
  
getNumChildrenForItem() returns the number of child (auto-aggreated)  
transactions the item at aIndex has.  
@param aIndex The index of the item in the list.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>The index of the item in the list.  
</td>
</tr>

</table>

### getChildListForItem(aIndex) ###
  
getChildListForItem() returns the list of children associated with the  
item at aIndex. Implementations may return null if there are no children,  
or an empty list. The list returned is AddRef'd so it is up to the caller  
to Release the transaction when it is done.  
@param aIndex The index of the item in the list.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>The index of the item in the list.  
</td>
</tr>

</table>

## Attributes ##

### numItems ###
  
The number of transactions contained in this list.  
  
