---
layout: default
---

# rdfITripleVisitor #
  
Interface used in RDF to enumerate triples.  
Also used by rdfIDataSource::getAllSubjects, then aPredicate,  
aObject and aTruthValue are ignored.  
  
@status PLASMA  
  

## Methods ##

### visit(aSubject, aPredicate, aObject, aTruthValue) ###
  
Callback function for returning query results.  
  
@param aSubject, aPredicate, aObject describe the (sub-)arc  
@returnCode NS_RDF_STOP_VISIT to stop iterating over the query result.  
            Any error code will stop the iteration as well.  
  

#### Parameters ####

<table>

<tr>
<td>aSubject,</td>
<td>aPredicate, aObject describe the (sub-)arc  
</td>
</tr>

</table>
