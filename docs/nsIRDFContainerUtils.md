---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFContainerUtils.idl">Source file</a>
</div>

# nsIRDFContainerUtils #

## Methods ##

### IsOrdinalProperty(aProperty) ###
  
Returns 'true' if the property is an RDF ordinal property.  
  

### IndexToOrdinalResource(aIndex) ###
  
Convert the specified index to an ordinal property.  
  

### OrdinalResourceToIndex(aOrdinal) ###
  
Convert the specified ordinal property into an index  
  

### IsContainer(aDataSource, aResource) ###
  
Return 'true' if the specified resource is a container  
  

### IsEmpty(aDataSource, aResource) ###
  
Return 'true' if the specified resource is a container and it is empty  
  

### IsBag(aDataSource, aResource) ###
  
Return 'true' if the specified resource is a bag  
  

### IsSeq(aDataSource, aResource) ###
  
Return 'true' if the specified resource is a sequence  
  

### IsAlt(aDataSource, aResource) ###
  
Return 'true' if the specified resource is an alternation  
  

### MakeBag(aDataSource, aResource) ###
  
Decorates the specified resource appropriately to make it  
usable as an empty bag in the specified data source.  
  

### MakeSeq(aDataSource, aResource) ###
  
Decorates the specified resource appropriately to make it  
usable as an empty sequence in the specified data source.  
  

### MakeAlt(aDataSource, aResource) ###
  
Decorates the specified resource appropriately to make it  
usable as an empty alternation in the specified data source.  
  

### indexOf(aDataSource, aContainer, aElement) ###
  
Retrieve the index of element in the container. Returns -1 if  
the element is not in the container.  
  
