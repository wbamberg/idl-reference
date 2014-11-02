---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFDataSource.idl">Source file</a>
</div>
# nsIRDFDataSource #

## Methods ##

### GetSource(aProperty, aTarget, aTruthValue) ###
 Find an RDF resource that points to a given node over the  
specified arc & truth value  
  
@throws NS_RDF_NO_VALUE if there is no source that leads  
to the target with the specified property.  
  

### GetSources(aProperty, aTarget, aTruthValue) ###
  
Find all RDF resources that point to a given node over the  
specified arc & truth value  
  

### GetTarget(aSource, aProperty, aTruthValue) ###
  
Find a child of that is related to the source by the given arc  
arc and truth value  
  
@throws NS_RDF_NO_VALUE if there is no target accessible from the  
source via the specified property.  
  

### GetTargets(aSource, aProperty, aTruthValue) ###
  
Find all children of that are related to the source by the given arc  
arc and truth value.  
  

### Assert(aSource, aProperty, aTarget, aTruthValue) ###
  
Add an assertion to the graph.  
  

### Unassert(aSource, aProperty, aTarget) ###
  
Remove an assertion from the graph.  
  

### Change(aSource, aProperty, aOldTarget, aNewTarget) ###
  
Change an assertion from  
  
  [aSource]--[aProperty]-->[aOldTarget]  
  
to  
  
  [aSource]--[aProperty]-->[aNewTarget]  
  

### Move(aOldSource, aNewSource, aProperty, aTarget) ###
  
'Move' an assertion from  
  
  [aOldSource]--[aProperty]-->[aTarget]  
  
to  
  
  [aNewSource]--[aProperty]-->[aTarget]  
  

### HasAssertion(aSource, aProperty, aTarget, aTruthValue) ###
  
Query whether an assertion exists in this graph.  
  

### AddObserver(aObserver) ###
  
Add an observer to this data source. If the datasource  
supports observers, the datasource source should hold a strong  
reference to the observer.  
  

### RemoveObserver(aObserver) ###
  
Remove an observer from this data source.  
  

### ArcLabelsIn(aNode) ###
  
Get a cursor to iterate over all the arcs that point into a node.  
  

### ArcLabelsOut(aSource) ###
  
Get a cursor to iterate over all the arcs that originate in  
a resource.  
  

### GetAllResources() ###
  
Retrieve all of the resources that the data source currently  
refers to.  
  

### IsCommandEnabled(aSources, aCommand, aArguments) ###
  
Returns whether a given command is enabled for a set of sources.   
  

### DoCommand(aSources, aCommand, aArguments) ###
  
Perform the specified command on set of sources.  
  

### GetAllCmds(aSource) ###
  
Returns the set of all commands defined for a given source.  
  

### hasArcIn(aNode, aArc) ###
  
Returns true if the specified node is pointed to by the specified arc.  
Equivalent to enumerating ArcLabelsIn and comparing for the specified arc.  
  

### hasArcOut(aSource, aArc) ###
  
Returns true if the specified node has the specified outward arc.  
Equivalent to enumerating ArcLabelsOut and comparing for the specified arc.  
  

### beginUpdateBatch() ###
  
Notify observers that the datasource is about to send several  
notifications at once.  
This must be followed by calling endUpdateBatch(), otherwise  
viewers will get out of sync.  
  

### endUpdateBatch() ###
  
Notify observers that the datasource has completed issuing  
a notification group.  
  

## Attributes ##

### URI ###
 The "URI" of the data source. This used by the RDF service's  
|GetDataSource()| method to cache datasources.  
  
