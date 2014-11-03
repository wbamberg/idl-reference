---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/dns/nsIDNSListener.idl">Source file</a>
</div>

# nsIDNSListener #
<code>  
nsIDNSListener  
  
</code>
## Methods ##

### onLookupComplete(aRequest, aRecord, aStatus) ###
<code>  
called when an asynchronous host lookup completes.  
  
@param aRequest  
       the value returned from asyncResolve.  
@param aRecord  
       the DNS record corresponding to the hostname that was resolved.  
       this parameter is null if there was an error.  
@param aStatus  
       if the lookup failed, this parameter gives the reason.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aRequest</td>
<td>       the value returned from asyncResolve.  
</td>
</tr>

<tr>
<td>aRecord</td>
<td>       the DNS record corresponding to the hostname that was resolved.  
       this parameter is null if there was an error.  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>       if the lookup failed, this parameter gives the reason.  
</td>
</tr>

</table>
