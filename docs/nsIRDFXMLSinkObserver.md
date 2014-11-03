---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFXMLSink.idl">Source file</a>
</div>

# nsIRDFXMLSinkObserver #
<code>  
An observer that is notified as progress is made on the load  
of an RDF/XML document in an <code>nsIRDFXMLSink</code>.  
  
</code>
## Methods ##

### onBeginLoad(aSink) ###
<code>  
Called when the load begins.  
@param aSink the RDF/XML sink on which the load is beginning.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>the RDF/XML sink on which the load is beginning.  
</td>
</tr>

</table>

### onInterrupt(aSink) ###
<code>  
Called when the load is suspended (e.g., for network quantization).  
@param aSink the RDF/XML sink that is being interrupted.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>the RDF/XML sink that is being interrupted.  
</td>
</tr>

</table>

### onResume(aSink) ###
<code>  
Called when a suspended load is resuming.  
@param aSink the RDF/XML sink that is resuming.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>the RDF/XML sink that is resuming.  
</td>
</tr>

</table>

### onEndLoad(aSink) ###
<code>  
Called when an RDF/XML load completes successfully.  
@param aSink the RDF/XML sink that has finished loading.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>the RDF/XML sink that has finished loading.  
</td>
</tr>

</table>

### onError(aSink, aStatus, aErrorMsg) ###
<code>  
Called when an error occurs during the load  
@param aSink the RDF/XML sink in which the error occurred  
@param aStatus the networking result code  
@param aErrorMsg an error message, if applicable  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSink</td>
<td>the RDF/XML sink in which the error occurred  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>the networking result code  
</td>
</tr>

<tr>
<td>aErrorMsg</td>
<td>an error message, if applicable  
</td>
</tr>

</table>
