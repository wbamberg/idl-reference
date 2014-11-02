---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/filewatcher/nsINativeFileWatcher.idl">Source file</a>
</div>
# nsINativeFileWatcherCallback #
  
The interface for the callback invoked when a change on a watched  
resource is detected.  
  

## Methods ##

### changed(resourcePath, flags) ###
  
@param resourcePath  
       The path of the changed resource. If there were too many changes,  
       the string "*" is passed.  
@param flags Reserved for future uses, not currently used.  
  

#### Parameters ####

<table>

<tr>
<td>resourcePath</td>
<td>       The path of the changed resource. If there were too many changes,  
       the string "*" is passed.  
</td>
</tr>

<tr>
<td>flags</td>
<td>Reserved for future uses, not currently used.  
</td>
</tr>

</table>
