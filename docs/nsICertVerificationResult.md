---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIX509Cert.idl">Source file</a>
</div>

# nsICertVerificationResult #

## Methods ##

### getUsagesArrayResult(verified, count, usages) ###
<pre>  
 This interface reflects a container of  
 verification results. Call will not block.  
  
 Obtain an array of human readable strings describing  
 the certificate's certified usages.  
  
 Mirrors the results produced by  
 nsIX509Cert::getUsagesArray()  
  
 As of today, this function is a one-shot object,  
 only the first call will succeed.  
 This allows an optimization in the implementation,  
 ownership of result data will be transfered to caller.  
  
 @param cert The certificate that was verified.  
 @param verified The certificate verification result,  
        see constants in nsIX509Cert.  
 @param count The number of human readable usages returned.  
 @param usages The array of human readable usages.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>cert</td>
<td>The certificate that was verified.  
</td>
</tr>

<tr>
<td>verified</td>
<td>The certificate verification result,  
        see constants in nsIX509Cert.  
</td>
</tr>

<tr>
<td>count</td>
<td>The number of human readable usages returned.  
</td>
</tr>

<tr>
<td>usages</td>
<td>The array of human readable usages.  
</td>
</tr>

</table>
