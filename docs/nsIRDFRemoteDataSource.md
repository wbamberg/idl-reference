---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFRemoteDataSource.idl">Source file</a>
</div>

# nsIRDFRemoteDataSource #
<pre>  
A datasource that may load asynchronously  
  
</pre>
## Methods ##

### Init(aURI) ###
<pre>  
Specify the URI for the data source: this is the prefix  
that will be used to register the data source in the  
data source registry.  
@param aURI the URI to load  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the URI to load  
</td>
</tr>

</table>

### Refresh(aBlocking) ###
<pre>  
Refresh the remote datasource, re-loading its contents  
from the URI.  
  
@param aBlocking If <code>true</code>, the call will block  
until the datasource has completely reloaded.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aBlocking</td>
<td>If <code>true</code>, the call will block  
until the datasource has completely reloaded.  
</td>
</tr>

</table>

### Flush() ###
<pre>  
Request that a data source write its contents out to   
permanent storage, if applicable.  
  
</pre>
### FlushTo(aURI) ###

## Attributes ##

### loaded ###
<pre>  
This value is <code>true</code> when the datasource has  
fully loaded itself.  
  
</pre>