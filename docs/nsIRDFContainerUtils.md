---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFContainerUtils.idl">Source file</a>
</div>

# nsIRDFContainerUtils #

## Methods ##

### IsOrdinalProperty(aProperty) ###
<code>  
Returns 'true' if the property is an RDF ordinal property.  
  
</code>
### IndexToOrdinalResource(aIndex) ###
<code>  
Convert the specified index to an ordinal property.  
  
</code>
### OrdinalResourceToIndex(aOrdinal) ###
<code>  
Convert the specified ordinal property into an index  
  
</code>
### IsContainer(aDataSource, aResource) ###
<code>  
Return 'true' if the specified resource is a container  
  
</code>
### IsEmpty(aDataSource, aResource) ###
<code>  
Return 'true' if the specified resource is a container and it is empty  
  
</code>
### IsBag(aDataSource, aResource) ###
<code>  
Return 'true' if the specified resource is a bag  
  
</code>
### IsSeq(aDataSource, aResource) ###
<code>  
Return 'true' if the specified resource is a sequence  
  
</code>
### IsAlt(aDataSource, aResource) ###
<code>  
Return 'true' if the specified resource is an alternation  
  
</code>
### MakeBag(aDataSource, aResource) ###
<code>  
Decorates the specified resource appropriately to make it  
usable as an empty bag in the specified data source.  
  
</code>
### MakeSeq(aDataSource, aResource) ###
<code>  
Decorates the specified resource appropriately to make it  
usable as an empty sequence in the specified data source.  
  
</code>
### MakeAlt(aDataSource, aResource) ###
<code>  
Decorates the specified resource appropriately to make it  
usable as an empty alternation in the specified data source.  
  
</code>
### indexOf(aDataSource, aContainer, aElement) ###
<code>  
Retrieve the index of element in the container. Returns -1 if  
the element is not in the container.  
  
</code>