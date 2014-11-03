---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/url-classifier/nsIUrlClassifierHashCompleter.idl">Source file</a>
</div>

# nsIUrlClassifierHashCompleterCallback #
<code>  
This interface is implemented by nsIUrlClassifierHashCompleter clients.  
  
</code>
## Methods ##

### completion(hash, table, chunkId) ###
<code>  
A complete hash has been found that matches the partial hash.  
This method may be called 0-n times for a given  
nsIUrlClassifierCompleter::complete() call.  
  
@param hash  
       The 128-bit hash that was discovered.  
@param table  
       The name of the table that this hash belongs to.  
@param chunkId  
       The database chunk that this hash belongs to.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>hash</td>
<td>       The 128-bit hash that was discovered.  
</td>
</tr>

<tr>
<td>table</td>
<td>       The name of the table that this hash belongs to.  
</td>
</tr>

<tr>
<td>chunkId</td>
<td>       The database chunk that this hash belongs to.  
</td>
</tr>

</table>

### completionFinished(status) ###
<code>  
The completion is complete.  This method is called once per  
nsIUrlClassifierCompleter::complete() call, after all completion()  
calls are finished.  
  
@param status  
       NS_OK if the request completed successfully, or an error code.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>status</td>
<td>       NS_OK if the request completed successfully, or an error code.  
</td>
</tr>

</table>
