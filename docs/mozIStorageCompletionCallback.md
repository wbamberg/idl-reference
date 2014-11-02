---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageCompletionCallback.idl">Source file</a>
</div>

# mozIStorageCompletionCallback #

## Methods ##

### complete(status, value) ###
  
Indicates that the event this callback was passed in for has completed.  
  
@param status  
       The status of the call. Generally NS_OK if the operation  
       completed successfully.  
@param value  
       If the operation produces a result, the result. Otherwise,  
       |null|.  
  
@see The calling method for expected values.  
  

#### Parameters ####

<table>

<tr>
<td>status</td>
<td>       The status of the call. Generally NS_OK if the operation  
       completed successfully.  
</td>
</tr>

<tr>
<td>value</td>
<td>       If the operation produces a result, the result. Otherwise,  
       |null|.  
</td>
</tr>

</table>
