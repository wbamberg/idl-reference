---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/url-classifier/nsIUrlClassifierHashCompleter.idl">Source file</a>
</div>

# nsIUrlClassifierHashCompleter #
  
Clients updating the url-classifier database have the option of sending  
partial (32-bit) hashes of URL fragments to be blacklisted.  If the  
url-classifier encounters one of these truncated hashes, it will ask an  
nsIUrlClassifierCompleter instance to asynchronously provide the complete  
hash, along with some associated metadata.  
This is only ever used for testing and should absolutely be deleted (I  
think).  
  

## Methods ##

### complete(partialHash, gethashUrl, callback) ###
  
Request a completed hash from the given gethash url.  
  
  

#### Parameters ####

<table>

<tr>
<td>partialHash</td>
<td>       The 32-bit hash encountered by the url-classifier.  
</td>
</tr>

<tr>
<td>gethashUrl</td>
<td>       The gethash url to use.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       An nsIUrlClassifierCompleterCallback instance.  
</td>
</tr>

</table>
