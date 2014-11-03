---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIBrowserSearchService.idl">Source file</a>
</div>

# nsISearchInstallCallback #

## Methods ##

### onSuccess(engine) ###
  
Called to indicate that the engine addition process succeeded.  
  
@param engine  
       The nsISearchEngine object that was added (will not be null).  
  

#### Parameters ####

<table>

<tr>
<td>engine</td>
<td>       The nsISearchEngine object that was added (will not be null).  
</td>
</tr>

</table>

### onError(errorCode) ###
  
Called to indicate that the engine addition process failed.  
  
@param errorCode  
       One of the ERROR_* values described above indicating the cause of  
       the failure.  
  

#### Parameters ####

<table>

<tr>
<td>errorCode</td>
<td>       One of the ERROR_* values described above indicating the cause of  
       the failure.  
</td>
</tr>

</table>

## Constants ##

### ERROR_UNKNOWN_FAILURE ###

### ERROR_DUPLICATE_ENGINE ###
