---
layout: default
---

# nsIClipboard #

## Methods ##

### setData(aTransferable, anOwner, aWhichClipboard) ###
  
Given a transferable, set the data on the native clipboard  
  
@param  aTransferable The transferable  
@param  anOwner The owner of the transferable  
@param  aWhichClipboard Specifies the clipboard to which this operation applies.  
@result NS_Ok if no errors  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aTransferable The transferable  
</td>
</tr>

<tr>
<td></td>
<td>aTransferable The transferable  
</td>
</tr>

<tr>
<td></td>
<td>aTransferable The transferable  
</td>
</tr>

</table>

### getData(aTransferable, aWhichClipboard) ###
  
Given a transferable, get the clipboard data.  
  
@param  aTransferable The transferable  
@param  aWhichClipboard Specifies the clipboard to which this operation applies.  
@result NS_Ok if no errors  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aTransferable The transferable  
</td>
</tr>

<tr>
<td></td>
<td>aTransferable The transferable  
</td>
</tr>

</table>

### emptyClipboard(aWhichClipboard) ###
  
This empties the clipboard and notifies the clipboard owner.  
This empties the "logical" clipboard. It does not clear the native clipboard.  
  
@param  aWhichClipboard Specifies the clipboard to which this operation applies.  
@result NS_OK if successful.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aWhichClipboard Specifies the clipboard to which this operation applies.  
@result NS_OK if successful.  
</td>
</tr>

</table>

### hasDataMatchingFlavors(aFlavorList, aLength, aWhichClipboard) ###
  
This provides a way to give correct UI feedback about, for instance, a paste   
should be allowed. It does _NOT_ actually retreive the data and should be a very  
inexpensive call. All it does is check if there is data on the clipboard matching  
any of the flavors in the given list.  
  
@param  aFlavorList     An array of ASCII strings.  
@param  aLength         The length of the aFlavorList.  
@param  aWhichClipboard Specifies the clipboard to which this operation applies.  
@outResult - if data is present matching one of   
@result NS_OK if successful.  
  

#### Parameters ####

<table>

<tr>
<td></td>
<td>aFlavorList     An array of ASCII strings.  
</td>
</tr>

<tr>
<td></td>
<td>aFlavorList     An array of ASCII strings.  
</td>
</tr>

<tr>
<td></td>
<td>aFlavorList     An array of ASCII strings.  
</td>
</tr>

</table>

### supportsSelectionClipboard() ###
  
Allows clients to determine if the implementation supports the concept of a   
separate clipboard for selection.  
  
@outResult - true if   
@result NS_OK if successful.  
  

### supportsFindClipboard() ###
  
Allows clients to determine if the implementation supports the concept of a  
separate clipboard for find search strings.  
  
@result NS_OK if successful.  
  

## Constants ##

### kSelectionClipboard ###

### kGlobalClipboard ###

### kFindClipboard ###
