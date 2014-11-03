---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFContainer.idl">Source file</a>
</div>

# nsIRDFContainer #

## Methods ##

### Init(aDataSource, aContainer) ###
<code>  
Initialize the container wrapper to the specified resource  
using the specified datasource for context.  
  
</code>
### GetCount() ###
<code>  
Return the number of elements in the container. Note that this  
may not always be accurate due to aggregation.  
  
</code>
### GetElements() ###
<code>  
Return an enumerator that can be used to enumerate the contents  
of the container in ascending order.  
  
</code>
### AppendElement(aElement) ###
<code>  
Append an element to the container, assigning it the next  
available ordinal.  
  
</code>
### RemoveElement(aElement, aRenumber) ###
<code>  
Remove the first occurence of the specified element from the  
container. If aRenumber is 'true', then the underlying RDF graph  
will be 're-numbered' to account for the removal.  
  
</code>
### InsertElementAt(aElement, aIndex, aRenumber) ###
<code>  
Insert aElement at the specified index. If aRenumber is 'true', then  
the underlying RDF graph will be 're-numbered' to accomodate the new  
element.  
  
</code>
### RemoveElementAt(aIndex, aRenumber) ###
<code>  
Remove the element at the specified index. If aRenumber is 'true', then  
the underlying RDF graph will be 're-numbered' to account for the  
removal.  
  
@return the element that was removed.  
  
</code>
#### Returns ####

<table>

<tr>
<td>the element that was removed.  
</td>
</tr>

</table>

### IndexOf(aElement) ###
<code>  
Determine the index of an element in the container.  
  
@return The index of the specified element in the container. If  
the element is not contained in the container, this function  
returns '-1'.  
  
</code>
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
