---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIAsyncLivemarks.idl">Source file</a>
</div>
# mozILivemarkCallback #

## Methods ##

### onCompletion(aStatus, aLivemark) ###
  
Invoked when a livemark is added, removed or retrieved.  
  
@param aStatus  
       Whether the request was completed successfully.  
       Use Components.isSuccessCode(aStatus) to check this.  
@param aLivemark  
       A mozILivemark object representing the livemark, or null on removal.  
  

#### Parameters ####

<table>

<tr>
<td>aStatus</td>
<td>       Whether the request was completed successfully.  
       Use Components.isSuccessCode(aStatus) to check this.  
</td>
</tr>

<tr>
<td>aLivemark</td>
<td>       A mozILivemark object representing the livemark, or null on removal.  
</td>
</tr>

</table>
