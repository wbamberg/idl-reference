---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFXMLSink.idl">Source file</a>
</div>

# nsIRDFXMLSink #
<pre>  
A "sink" that receives and processes RDF/XML. This interface is used  
by the RDF/XML parser.  
  
</pre>
## Methods ##

### beginLoad() ###
<pre>  
Initiate the RDF/XML load.  
  
</pre>
### interrupt() ###
<pre>  
Suspend the RDF/XML load.  
  
</pre>
### resume() ###
<pre>  
Resume the RDF/XML load.  
  
</pre>
### endLoad() ###
<pre>  
Complete the RDF/XML load.  
  
</pre>
### addNameSpace(aPrefix, aURI) ###
<pre>  
Add namespace information to the RDF/XML sink.  
@param aPrefix the namespace prefix  
@param aURI the namespace URI  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aPrefix</td>
<td>the namespace prefix  
</td>
</tr>

<tr>
<td>aURI</td>
<td>the namespace URI  
</td>
</tr>

</table>

### addXMLSinkObserver(aObserver) ###
<pre>  
Add an observer that will be notified as the RDF/XML load  
progresses.  
<p>  
  
Note that the sink will acquire a strong reference to the  
observer, so care should be taken to avoid cyclical references  
that cannot be released (i.e., if the observer holds a  
reference to the sink, it should be sure that it eventually  
clears the reference).  
  
@param aObserver the observer to add to the sink's set of  
load observers.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>the observer to add to the sink's set of  
load observers.  
</td>
</tr>

</table>

### removeXMLSinkObserver(aObserver) ###
<pre>  
Remove an observer from the sink's set of observers.  
@param aObserver the observer to remove.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>the observer to remove.  
</td>
</tr>

</table>

## Attributes ##

### readOnly ###
<pre>  
Set to <code>true</code> if the sink is read-only and cannot  
be modified  
  
</pre>