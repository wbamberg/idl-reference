---
layout: default
---

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
  
@return the element that was removed.  
  

### IndexOf(aElement) ###
  
Determine the index of an element in the container.  
  
@return The index of the specified element in the container. If  
the element is not contained in the container, this function  
returns '-1'.  
  

## Attributes ##

### DataSource ###

### Resource ###
