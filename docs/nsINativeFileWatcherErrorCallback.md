---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/filewatcher/nsINativeFileWatcher.idl">Source file</a>
</div>

# nsINativeFileWatcherErrorCallback #
<code>  
The interface for the callback invoked when there is an error.  
  
</code>
## Methods ##

### complete(xpcomError, osError) ###
<code>  
@param xpcomError The XPCOM error code.  
@param osError The native OS error (errno under Unix, GetLastError under Windows).  
  
</code>
#### Parameters ####

<table>

<tr>
<td>xpcomError</td>
<td>The XPCOM error code.  
</td>
</tr>

<tr>
<td>osError</td>
<td>The native OS error (errno under Unix, GetLastError under Windows).  
</td>
</tr>

</table>
