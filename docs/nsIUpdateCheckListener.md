---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/update/nsIUpdateService.idl">Source file</a>
</div>

# nsIUpdateCheckListener #
<code>  
An interface describing an object that listens to the progress of an update  
check operation. This object is notified as the check continues, finishes  
and if it has an error.  
  
</code>
## Methods ##

### onCheckComplete(request, updates, updateCount) ###
<code>  
The update check was completed.  
@param   request  
         The nsIXMLHttpRequest handling the update check.  
@param   updates  
         An array of nsIUpdate objects listing available updates.  
@param   updateCount  
         The size of the |updates| array.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>request</td>
<td>         The nsIXMLHttpRequest handling the update check.  
</td>
</tr>

<tr>
<td>updates</td>
<td>         An array of nsIUpdate objects listing available updates.  
</td>
</tr>

<tr>
<td>updateCount</td>
<td>         The size of the |updates| array.  
</td>
</tr>

</table>

### onError(request, update) ###
<code>  
An error occurred while loading the remote update service file.  
@param   request  
         The nsIXMLHttpRequest handling the update check.  
@param   update  
         A nsIUpdate object that contains details about the  
         error in its |statusText| property.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>request</td>
<td>         The nsIXMLHttpRequest handling the update check.  
</td>
</tr>

<tr>
<td>update</td>
<td>         A nsIUpdate object that contains details about the  
         error in its |statusText| property.  
</td>
</tr>

</table>
