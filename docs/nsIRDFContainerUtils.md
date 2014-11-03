---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFContainerUtils.idl">Source file</a>
</div>

# nsIRDFContainerUtils #

## Methods ##

### IsOrdinalProperty(aProperty) ###
<pre>  
Returns 'true' if the property is an RDF ordinal property.  
  
</pre>
### IndexToOrdinalResource(aIndex) ###
<pre>  
Convert the specified index to an ordinal property.  
  
</pre>
### OrdinalResourceToIndex(aOrdinal) ###
<pre>  
Convert the specified ordinal property into an index  
  
</pre>
### IsContainer(aDataSource, aResource) ###
<pre>  
Return 'true' if the specified resource is a container  
  
</pre>
### IsEmpty(aDataSource, aResource) ###
<pre>  
Return 'true' if the specified resource is a container and it is empty  
  
</pre>
### IsBag(aDataSource, aResource) ###
<pre>  
Return 'true' if the specified resource is a bag  
  
</pre>
### IsSeq(aDataSource, aResource) ###
<pre>  
Return 'true' if the specified resource is a sequence  
  
</pre>
### IsAlt(aDataSource, aResource) ###
<pre>  
Return 'true' if the specified resource is an alternation  
  
</pre>
### MakeBag(aDataSource, aResource) ###
<pre>  
Decorates the specified resource appropriately to make it  
usable as an empty bag in the specified data source.  
  
</pre>
### MakeSeq(aDataSource, aResource) ###
<pre>  
Decorates the specified resource appropriately to make it  
usable as an empty sequence in the specified data source.  
  
</pre>
### MakeAlt(aDataSource, aResource) ###
<pre>  
Decorates the specified resource appropriately to make it  
usable as an empty alternation in the specified data source.  
  
</pre>
### indexOf(aDataSource, aContainer, aElement) ###
<pre>  
Retrieve the index of element in the container. Returns -1 if  
the element is not in the container.  
  
</pre>