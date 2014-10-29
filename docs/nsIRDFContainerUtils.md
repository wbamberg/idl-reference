---
layout: default
---

# nsIRDFContainerUtils #

## IsOrdinalProperty ##

Returns 'true' if the property is an RDF ordinal property.


## IndexToOrdinalResource ##

Convert the specified index to an ordinal property.


## OrdinalResourceToIndex ##

Convert the specified ordinal property into an index


## IsContainer ##

Return 'true' if the specified resource is a container


## IsEmpty ##

Return 'true' if the specified resource is a container and it is empty


## IsBag ##

Return 'true' if the specified resource is a bag


## IsSeq ##

Return 'true' if the specified resource is a sequence


## IsAlt ##

Return 'true' if the specified resource is an alternation


## MakeBag ##

Decorates the specified resource appropriately to make it
usable as an empty bag in the specified data source.


## MakeSeq ##

Decorates the specified resource appropriately to make it
usable as an empty sequence in the specified data source.


## MakeAlt ##

Decorates the specified resource appropriately to make it
usable as an empty alternation in the specified data source.


## indexOf ##

Retrieve the index of element in the container. Returns -1 if
the element is not in the container.

