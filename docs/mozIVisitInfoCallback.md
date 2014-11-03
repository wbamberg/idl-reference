---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIAsyncHistory.idl">Source file</a>
</div>

# mozIVisitInfoCallback #
<pre>  
Shared Callback interface for mozIAsyncHistory methods. The semantics  
for each method are detailed in mozIAsyncHistory.  
  
</pre>
## Methods ##

### handleError(aResultCode, aPlaceInfo) ###
<pre>  
Called when the given place could not be processed.  
  
@param aResultCode  
       nsresult indicating the failure reason.  
@param aPlaceInfo  
       The information that was given to the caller for the place.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aResultCode</td>
<td>       nsresult indicating the failure reason.  
</td>
</tr>

<tr>
<td>aPlaceInfo</td>
<td>       The information that was given to the caller for the place.  
</td>
</tr>

</table>

### handleResult(aPlaceInfo) ###
<pre>  
Called for each place processed successfully.  
  
@param aPlaceInfo  
       The current info stored for the place.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aPlaceInfo</td>
<td>       The current info stored for the place.  
</td>
</tr>

</table>

### handleCompletion() ###
<pre>  
Called when all records were processed.  
  
</pre>