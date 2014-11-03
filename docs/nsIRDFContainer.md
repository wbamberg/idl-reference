---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFContainer.idl">Source file</a>
</div>

# nsIRDFContainer #

## Methods ##

### Init(aDataSource, aContainer) ###
  
Initialize the container wrapper to the specified resource  
using the specified datasource for context.  
  

### GetCount() ###
  
Return the number of elements in the container. Note that this  
may not always be accurate due to aggregation.  
  

### GetElements() ###
  
Return an enumerator that can be used to enumerate the contents  
of the container in ascending order.  
  

### AppendElement(aElement) ###
  
Append an element to the container, assigning it the next  
available ordinal.  
  

### RemoveElement(aElement, aRenumber) ###
  
Remove the first occurence of the specified element from the  
container. If aRenumber is 'true', then the underlying RDF graph  
will be 're-numbered' to account for the removal.  
  

### InsertElementAt(aElement, aIndex, aRenumber) ###
  
Insert aElement at the specified index. If aRenumber is 'true', then  
the underlying RDF graph will be 're-numbered' to accomodate the new  
element.  
  

### RemoveElementAt(aIndex, aRenumber) ###
  
Remove the element at the specified index. If aRenumber is 'true', then  
the underlying RDF graph will be 're-numbered' to account for the  
removal.  
  
  

#### Returns ####

<table>

<tr>
<td>the element that was removed.  
</td>
</tr>

</table>

### IndexOf(aElement) ###
  
Determine the index of an element in the container.  
  
  

#### Returns ####

<table>

<tr>
<td>The index of the specified element in the container. If  
the element is not contained in the container, this function  
returns '-1'.  
</td>
</tr>

</table>

## Attributes ##

### DataSource ###

### Resource ###
