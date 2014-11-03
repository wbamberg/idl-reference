---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFXMLParser.idl">Source file</a>
</div>

# nsIRDFXMLParser #

## Methods ##

### parseAsync(aSink, aBaseURI) ###
<code>  
Create a stream listener that can be used to asynchronously  
parse RDF/XML.  
@param aSink the RDF datasource the will receive the data  
@param aBaseURI the base URI used to resolve relative  
  references in the RDF/XML  
@return an nsIStreamListener object to handle the data  
  
</code>
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
<code>  
Parse a string of RDF/XML  
@param aSink the RDF datasource that will receive the data  
@param aBaseURI the base URI used to resolve relative  
  references in the RDF/XML  
@param aSource a UTF8 string containing RDF/XML data.  
  
</code>
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
