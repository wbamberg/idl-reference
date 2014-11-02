---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/rdfISerializer.idl">Source file</a>
</div>

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
  

#### Parameters ####

<table>

<tr>
<td>aDataSource</td>
<td>The RDF data source to be serialized.  
</td>
</tr>

<tr>
<td>aOut</td>
<td>The output stream to use.  
</td>
</tr>

</table>
