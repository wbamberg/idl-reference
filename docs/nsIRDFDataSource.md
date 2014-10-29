---
layout: default
---

# nsIRDFDataSource #

## Methods ##

### GetSource ###
 Find an RDF resource that points to a given node over the
specified arc & truth value

@throws NS_RDF_NO_VALUE if there is no source that leads
to the target with the specified property.


### GetSources ###

Find all RDF resources that point to a given node over the
specified arc & truth value


### GetTarget ###

Find a child of that is related to the source by the given arc
arc and truth value

@throws NS_RDF_NO_VALUE if there is no target accessible from the
source via the specified property.


### GetTargets ###

Find all children of that are related to the source by the given arc
arc and truth value.


### Assert ###

Add an assertion to the graph.


### Unassert ###

Remove an assertion from the graph.


### Change ###

Change an assertion from

  [aSource]--[aProperty]-->[aOldTarget]

to

  [aSource]--[aProperty]-->[aNewTarget]


### Move ###

'Move' an assertion from

  [aOldSource]--[aProperty]-->[aTarget]

to

  [aNewSource]--[aProperty]-->[aTarget]


### HasAssertion ###

Query whether an assertion exists in this graph.


### AddObserver ###

Add an observer to this data source. If the datasource
supports observers, the datasource source should hold a strong
reference to the observer.


### RemoveObserver ###

Remove an observer from this data source.


### ArcLabelsIn ###

Get a cursor to iterate over all the arcs that point into a node.


### ArcLabelsOut ###

Get a cursor to iterate over all the arcs that originate in
a resource.


### GetAllResources ###

Retrieve all of the resources that the data source currently
refers to.


### IsCommandEnabled ###

Returns whether a given command is enabled for a set of sources. 


### DoCommand ###

Perform the specified command on set of sources.


### GetAllCmds ###

Returns the set of all commands defined for a given source.


### hasArcIn ###

Returns true if the specified node is pointed to by the specified arc.
Equivalent to enumerating ArcLabelsIn and comparing for the specified arc.


### hasArcOut ###

Returns true if the specified node has the specified outward arc.
Equivalent to enumerating ArcLabelsOut and comparing for the specified arc.


### beginUpdateBatch ###

Notify observers that the datasource is about to send several
notifications at once.
This must be followed by calling endUpdateBatch(), otherwise
viewers will get out of sync.


### endUpdateBatch ###

Notify observers that the datasource has completed issuing
a notification group.


## Attributes ##

### URI ###
 The "URI" of the data source. This used by the RDF service's
|GetDataSource()| method to cache datasources.

