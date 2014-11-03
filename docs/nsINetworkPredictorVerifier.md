---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsINetworkPredictorVerifier.idl">Source file</a>
</div>

# nsINetworkPredictorVerifier #

## Methods ##

### onPredictPreconnect(uri) ###
<code>  
Callback for when we do a predictive preconnect  
  
@param uri - The URI that was preconnected to  
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>- The URI that was preconnected to  
</td>
</tr>

</table>

### onPredictDNS(uri) ###
<code>  
Callback for when we do a predictive DNS lookup  
  
@param uri - The URI that was looked up  
  
</code>
#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>- The URI that was looked up  
</td>
</tr>

</table>
