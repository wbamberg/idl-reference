---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/exthandler/nsIExternalHelperAppService.idl">Source file</a>
</div>

# nsPIExternalAppLauncher #
<pre>  
This is a private interface shared between external app handlers and the platform specific  
external helper app service  
  
</pre>
## Methods ##

### deleteTemporaryFileOnExit(aTemporaryFile) ###
<pre>  
mscott --> eventually I should move this into a new service so other  
consumers can add temporary files they want deleted on exit.  
@param aTemporaryFile A temporary file we should delete on exit.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aTemporaryFile</td>
<td>A temporary file we should delete on exit.  
</td>
</tr>

</table>

### deleteTemporaryPrivateFileWhenPossible(aTemporaryFile) ###
<pre>  
Delete a temporary file created inside private browsing mode when  
the private browsing mode has ended.  
  
</pre>