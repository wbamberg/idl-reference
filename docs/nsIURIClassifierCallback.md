---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIURIClassifier.idl">Source file</a>
</div>

# nsIURIClassifierCallback #
<pre>  
Callback function for nsIURIClassifier lookups.  
  
</pre>
## Methods ##

### onClassifyComplete(aErrorCode) ###
<pre>  
Called by the URI classifier service when it is done checking a URI.  
  
Clients are responsible for associating callback objects with classify()  
calls.  
  
@param aErrorCode  
       The error code with which the channel should be cancelled, or  
       NS_OK if the load should continue normally.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aErrorCode</td>
<td>       The error code with which the channel should be cancelled, or  
       NS_OK if the load should continue normally.  
</td>
</tr>

</table>
