---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/osfile/nsINativeOSFileInternals.idl">Source file</a>
</div>

# nsINativeOSFileErrorCallback #
  
A callback invoked in case of error.  
  

## Methods ##

### complete(operation, OSstatus) ###
  
  

#### Parameters ####

<table>

<tr>
<td>operation</td>
<td>The name of the failed operation. Provided to aid  
debugging only, may change without notice.  
</td>
</tr>

<tr>
<td>OSstatus</td>
<td>The OS status of the operation (errno under Unix,  
GetLastError under Windows).  
</td>
</tr>

</table>
