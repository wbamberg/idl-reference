---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/rdfIDataSource.idl">Source file</a>
</div>

# rdfIDataSource #
<code>  
Interface used in RDF to describe data sources.  
  
@status PLASMA  
  
</code>
## Methods ##

### visitAllSubjects(aVisitor) ###
<code>  
Visit all the subject resources in the datasource. The order is  
intederminate and may change from one invocation to the next.  
The subjects will be in the aSubject argument in calls into  
aVisitor, aPredicate and aObject will be null.  
@note Implementations may throw NS_ERROR_NOT_IMPLEMENTED for  
this method, but in this case RDF serializations of this  
datasource will not be possible.  
  
</code>
### visitAllTriples(aVisitor) ###
<code>  
Visit all the triples in the datasource. The order is  
intederminate and may change from one invocation to the next.  
@note Implementations may throw NS_ERROR_NOT_IMPLEMENTED for  
this method, but in this case RDF serializations of this  
datasource will not be possible.  
  
</code>