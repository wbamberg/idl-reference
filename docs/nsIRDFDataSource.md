---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFDataSource.idl">Source file</a>
</div>

# nsIRDFDataSource #

## Methods ##

### GetSource(aProperty, aTarget, aTruthValue) ###
<code> Find an RDF resource that points to a given node over the  
specified arc & truth value  
  
@throws NS_RDF_NO_VALUE if there is no source that leads  
to the target with the specified property.  
  
</code>
### GetSources(aProperty, aTarget, aTruthValue) ###
<code>  
Find all RDF resources that point to a given node over the  
specified arc & truth value  
  
</code>
### GetTarget(aSource, aProperty, aTruthValue) ###
<code>  
Find a child of that is related to the source by the given arc  
arc and truth value  
  
@throws NS_RDF_NO_VALUE if there is no target accessible from the  
source via the specified property.  
  
</code>
### GetTargets(aSource, aProperty, aTruthValue) ###
<code>  
Find all children of that are related to the source by the given arc  
arc and truth value.  
  
</code>
### Assert(aSource, aProperty, aTarget, aTruthValue) ###
<code>  
Add an assertion to the graph.  
  
</code>
### Unassert(aSource, aProperty, aTarget) ###
<code>  
Remove an assertion from the graph.  
  
</code>
### Change(aSource, aProperty, aOldTarget, aNewTarget) ###
<code>  
Change an assertion from  
  
  [aSource]--[aProperty]-->[aOldTarget]  
  
to  
  
  [aSource]--[aProperty]-->[aNewTarget]  
  
</code>
### Move(aOldSource, aNewSource, aProperty, aTarget) ###
<code>  
'Move' an assertion from  
  
  [aOldSource]--[aProperty]-->[aTarget]  
  
to  
  
  [aNewSource]--[aProperty]-->[aTarget]  
  
</code>
### HasAssertion(aSource, aProperty, aTarget, aTruthValue) ###
<code>  
Query whether an assertion exists in this graph.  
  
</code>
### AddObserver(aObserver) ###
<code>  
Add an observer to this data source. If the datasource  
supports observers, the datasource source should hold a strong  
reference to the observer.  
  
</code>
### RemoveObserver(aObserver) ###
<code>  
Remove an observer from this data source.  
  
</code>
### ArcLabelsIn(aNode) ###
<code>  
Get a cursor to iterate over all the arcs that point into a node.  
  
</code>
### ArcLabelsOut(aSource) ###
<code>  
Get a cursor to iterate over all the arcs that originate in  
a resource.  
  
</code>
### GetAllResources() ###
<code>  
Retrieve all of the resources that the data source currently  
refers to.  
  
</code>
### IsCommandEnabled(aSources, aCommand, aArguments) ###
<code>  
Returns whether a given command is enabled for a set of sources.   
  
</code>
### DoCommand(aSources, aCommand, aArguments) ###
<code>  
Perform the specified command on set of sources.  
  
</code>
### GetAllCmds(aSource) ###
<code>  
Returns the set of all commands defined for a given source.  
  
</code>
### hasArcIn(aNode, aArc) ###
<code>  
Returns true if the specified node is pointed to by the specified arc.  
Equivalent to enumerating ArcLabelsIn and comparing for the specified arc.  
  
</code>
### hasArcOut(aSource, aArc) ###
<code>  
Returns true if the specified node has the specified outward arc.  
Equivalent to enumerating ArcLabelsOut and comparing for the specified arc.  
  
</code>
### beginUpdateBatch() ###
<code>  
Notify observers that the datasource is about to send several  
notifications at once.  
This must be followed by calling endUpdateBatch(), otherwise  
viewers will get out of sync.  
  
</code>
### endUpdateBatch() ###
<code>  
Notify observers that the datasource has completed issuing  
a notification group.  
  
</code>
## Attributes ##

### URI ###
 The "URI" of the data source. This used by the RDF service's  
|GetDataSource()| method to cache datasources.  
  
