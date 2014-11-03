---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFDataSource.idl">Source file</a>
</div>

# nsIRDFDataSource #

## Methods ##

### GetSource(aProperty, aTarget, aTruthValue) ###
<pre> Find an RDF resource that points to a given node over the  
specified arc & truth value  
  
@throws NS_RDF_NO_VALUE if there is no source that leads  
to the target with the specified property.  
  
</pre>
### GetSources(aProperty, aTarget, aTruthValue) ###
<pre>  
Find all RDF resources that point to a given node over the  
specified arc & truth value  
  
</pre>
### GetTarget(aSource, aProperty, aTruthValue) ###
<pre>  
Find a child of that is related to the source by the given arc  
arc and truth value  
  
@throws NS_RDF_NO_VALUE if there is no target accessible from the  
source via the specified property.  
  
</pre>
### GetTargets(aSource, aProperty, aTruthValue) ###
<pre>  
Find all children of that are related to the source by the given arc  
arc and truth value.  
  
</pre>
### Assert(aSource, aProperty, aTarget, aTruthValue) ###
<pre>  
Add an assertion to the graph.  
  
</pre>
### Unassert(aSource, aProperty, aTarget) ###
<pre>  
Remove an assertion from the graph.  
  
</pre>
### Change(aSource, aProperty, aOldTarget, aNewTarget) ###
<pre>  
Change an assertion from  
  
  [aSource]--[aProperty]-->[aOldTarget]  
  
to  
  
  [aSource]--[aProperty]-->[aNewTarget]  
  
</pre>
### Move(aOldSource, aNewSource, aProperty, aTarget) ###
<pre>  
'Move' an assertion from  
  
  [aOldSource]--[aProperty]-->[aTarget]  
  
to  
  
  [aNewSource]--[aProperty]-->[aTarget]  
  
</pre>
### HasAssertion(aSource, aProperty, aTarget, aTruthValue) ###
<pre>  
Query whether an assertion exists in this graph.  
  
</pre>
### AddObserver(aObserver) ###
<pre>  
Add an observer to this data source. If the datasource  
supports observers, the datasource source should hold a strong  
reference to the observer.  
  
</pre>
### RemoveObserver(aObserver) ###
<pre>  
Remove an observer from this data source.  
  
</pre>
### ArcLabelsIn(aNode) ###
<pre>  
Get a cursor to iterate over all the arcs that point into a node.  
  
</pre>
### ArcLabelsOut(aSource) ###
<pre>  
Get a cursor to iterate over all the arcs that originate in  
a resource.  
  
</pre>
### GetAllResources() ###
<pre>  
Retrieve all of the resources that the data source currently  
refers to.  
  
</pre>
### IsCommandEnabled(aSources, aCommand, aArguments) ###
<pre>  
Returns whether a given command is enabled for a set of sources.   
  
</pre>
### DoCommand(aSources, aCommand, aArguments) ###
<pre>  
Perform the specified command on set of sources.  
  
</pre>
### GetAllCmds(aSource) ###
<pre>  
Returns the set of all commands defined for a given source.  
  
</pre>
### hasArcIn(aNode, aArc) ###
<pre>  
Returns true if the specified node is pointed to by the specified arc.  
Equivalent to enumerating ArcLabelsIn and comparing for the specified arc.  
  
</pre>
### hasArcOut(aSource, aArc) ###
<pre>  
Returns true if the specified node has the specified outward arc.  
Equivalent to enumerating ArcLabelsOut and comparing for the specified arc.  
  
</pre>
### beginUpdateBatch() ###
<pre>  
Notify observers that the datasource is about to send several  
notifications at once.  
This must be followed by calling endUpdateBatch(), otherwise  
viewers will get out of sync.  
  
</pre>
### endUpdateBatch() ###
<pre>  
Notify observers that the datasource has completed issuing  
a notification group.  
  
</pre>
## Attributes ##

### URI ###
<pre> The "URI" of the data source. This used by the RDF service's  
|GetDataSource()| method to cache datasources.  
  
</pre>