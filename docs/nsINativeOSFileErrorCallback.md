---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/osfile/nsINativeOSFileInternals.idl">Source file</a>
</div>

# nsINativeOSFileErrorCallback #
<pre>  
A callback invoked in case of error.  
  
</pre>
## Methods ##

### complete(operation, OSstatus) ###
<pre>  
@param operation The name of the failed operation. Provided to aid  
debugging only, may change without notice.  
@param OSstatus The OS status of the operation (errno under Unix,  
GetLastError under Windows).  
  
</pre>
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
