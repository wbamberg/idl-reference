---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/image/public/imgIOnloadBlocker.idl">Source file</a>
</div>

# imgIOnloadBlocker #

## Methods ##

### blockOnload(aRequest) ###
<pre>  
blockOnload  
Called when it is appropriate to block onload for the given imgIRequest.  
  
@param aRequest  
       The request that should block onload.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>       The request that should block onload.  
</td>
</tr>

</table>

### unblockOnload(aRequest) ###
<pre>  
unblockOnload  
Called when it is appropriate to unblock onload for the given  
imgIRequest.  
  
@param aRequest  
       The request that should unblock onload.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>       The request that should unblock onload.  
</td>
</tr>

</table>
