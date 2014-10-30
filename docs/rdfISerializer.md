---
layout: default
---

# rdfISerializer #
  
Interface used to serialize RDF.  
  
@status PLASMA  
  

## Methods ##

### serialize(aDataSource, aOut) ###
  
Synchronously serialize the given datasource to the outputstream.  
  
Implementations are not required to implement any buffering or  
other stream-based optimizations.  
  
@param aDataSource The RDF data source to be serialized.  
@param aOut The output stream to use.  
  
