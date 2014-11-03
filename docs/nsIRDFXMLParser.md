---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFXMLParser.idl">Source file</a>
</div>

# nsIRDFXMLParser #

## Methods ##

### parseAsync(aSink, aBaseURI) ###
  
Create a stream listener that can be used to asynchronously  
parse RDF/XML.  
  

#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>the RDF datasource the will receive the data  
</td>
</tr>

<tr>
<td>aBaseURI</td>
<td>the base URI used to resolve relative  
  references in the RDF/XML  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>an nsIStreamListener object to handle the data  
</td>
</tr>

</table>

### parseString(aSink, aBaseURI, aSource) ###
  
Parse a string of RDF/XML  
  

#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>the RDF datasource that will receive the data  
</td>
</tr>

<tr>
<td>aBaseURI</td>
<td>the base URI used to resolve relative  
  references in the RDF/XML  
</td>
</tr>

<tr>
<td>aSource</td>
<td>a UTF8 string containing RDF/XML data.  
</td>
</tr>

</table>
