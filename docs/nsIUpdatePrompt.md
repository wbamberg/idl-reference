---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/mozapps/update/nsIUpdateService.idl">Source file</a>
</div>

# nsIUpdatePrompt #
<pre>  
An interface describing an object that can show various kinds of Update  
notification UI to the user.  
  
</pre>
## Methods ##

### checkForUpdates() ###
<pre>  
Shows the application update checking user interface and checks if there  
is an update available.  
  
</pre>
### showUpdateAvailable(update) ###
<pre>  
Shows the application update available user interface advising that an  
update is available for download and install. If the app.update.silent  
preference is true or the user interface is already displayed the call will  
be a no-op.  
@param   update  
         The nsIUpdate object to be downloaded and installed  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>update</td>
<td>         The nsIUpdate object to be downloaded and installed  
</td>
</tr>

</table>

### showUpdateDownloaded(update, background) ###
<pre>  
Shows the application update downloaded user interface advising that an  
update has now been downloaded and a restart is necessary to complete the  
update. If background is true (e.g. the download was not user initiated)  
and the app.update.silent preference is true the call will be a no-op.  
@param   update  
         The nsIUpdate object that was downloaded  
@param   background  
         Less obtrusive UI, starting with a non-modal notification alert  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>update</td>
<td>         The nsIUpdate object that was downloaded  
</td>
</tr>

<tr>
<td>background</td>
<td>         Less obtrusive UI, starting with a non-modal notification alert  
</td>
</tr>

</table>

### showUpdateInstalled() ###
<pre>  
Shows the application update installed user interface advising that an  
update was installed successfully. If the app.update.silent preference is  
true, the app.update.showInstalledUI preference is false, or the user  
interface is already displayed the call will be a no-op.  
  
</pre>
### showUpdateError(update) ###
<pre>  
Shows the application update error user interface advising that an error  
occurred while checking for or applying an update. If the app.update.silent  
preference is true the call will be a no-op.  
@param   update  
         An nsIUpdate object representing the update that could not be  
         installed. The nsIUpdate object will not be the actual update when  
         the error occurred during an update check and will instead be an  
         nsIUpdate object with the error information for the update check.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>update</td>
<td>         An nsIUpdate object representing the update that could not be  
         installed. The nsIUpdate object will not be the actual update when  
         the error occurred during an update check and will instead be an  
         nsIUpdate object with the error information for the update check.  
</td>
</tr>

</table>

### showUpdateHistory(parent) ###
<pre>  
Shows a list of all updates installed to date.  
@param   parent  
         An nsIDOMWindow to set as the parent for this window. Can be null.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>parent</td>
<td>         An nsIDOMWindow to set as the parent for this window. Can be null.  
</td>
</tr>

</table>
