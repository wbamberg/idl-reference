---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageProgressHandler.idl">Source file</a>
</div>

# mozIStorageProgressHandler #
<pre>  
mozIProgressHandler is to be implemented by storage consumers that  
wish to receive callbacks during the request execution.  
  
</pre>
## Methods ##

### onProgress(aConnection) ###
<pre>  
onProgress is invoked periodically during long running calls.  
  
@param aConnection    connection, for which progress handler is  
                      invoked.  
  
@return true to abort request, false to continue work.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aConnection</td>
<td>connection, for which progress handler is  
                      invoked.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true to abort request, false to continue work.  
</td>
</tr>

</table>
