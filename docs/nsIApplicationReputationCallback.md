---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/downloads/nsIApplicationReputation.idl">Source file</a>
</div>

# nsIApplicationReputationCallback #

## Methods ##

### onComplete(aShouldBlock, aStatus) ###
  
Callback for the result of the application reputation query.  
  

#### Parameters ####

<table>

<tr>
<td>aStatus</td>
<td>       NS_OK if and only if the query succeeded. If it did, then  
       shouldBlock is meaningful (otherwise it defaults to false). This  
       may be NS_ERROR_FAILURE if the response cannot be parsed, or  
       NS_ERROR_NOT_AVAILABLE if the service has been disabled or is not  
       reachable.  
</td>
</tr>

<tr>
<td>aShouldBlock</td>
<td>       Whether or not the download should be blocked.  
</td>
</tr>

</table>
