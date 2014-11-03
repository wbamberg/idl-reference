---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIURIClassifier.idl">Source file</a>
</div>

# nsIURIClassifierCallback #
  
Callback function for nsIURIClassifier lookups.  
  

## Methods ##

### onClassifyComplete(aErrorCode) ###
  
Called by the URI classifier service when it is done checking a URI.  
  
Clients are responsible for associating callback objects with classify()  
calls.  
  
  

#### Parameters ####

<table>

<tr>
<td>aErrorCode</td>
<td>       The error code with which the channel should be cancelled, or  
       NS_OK if the load should continue normally.  
</td>
</tr>

</table>
