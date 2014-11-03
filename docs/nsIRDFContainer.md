---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFContainer.idl">Source file</a>
</div>

# nsIRDFContainer #

## Methods ##

### Init(aDataSource, aContainer) ###
<pre>  
Initialize the container wrapper to the specified resource  
using the specified datasource for context.  
  
</pre>
### GetCount() ###
<pre>  
Return the number of elements in the container. Note that this  
may not always be accurate due to aggregation.  
  
</pre>
### GetElements() ###
<pre>  
Return an enumerator that can be used to enumerate the contents  
of the container in ascending order.  
  
</pre>
### AppendElement(aElement) ###
<pre>  
Append an element to the container, assigning it the next  
available ordinal.  
  
</pre>
### RemoveElement(aElement, aRenumber) ###
<pre>  
Remove the first occurence of the specified element from the  
container. If aRenumber is 'true', then the underlying RDF graph  
will be 're-numbered' to account for the removal.  
  
</pre>
### InsertElementAt(aElement, aIndex, aRenumber) ###
<pre>  
Insert aElement at the specified index. If aRenumber is 'true', then  
the underlying RDF graph will be 're-numbered' to accomodate the new  
element.  
  
</pre>
### RemoveElementAt(aIndex, aRenumber) ###
<pre>  
Remove the element at the specified index. If aRenumber is 'true', then  
the underlying RDF graph will be 're-numbered' to account for the  
removal.  
  
@return the element that was removed.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>the element that was removed.  
</td>
</tr>

</table>

### IndexOf(aElement) ###
<pre>  
Determine the index of an element in the container.  
  
@return The index of the specified element in the container. If  
the element is not contained in the container, this function  
returns '-1'.  
  
</pre>
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
