---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/exthandler/nsIExternalHelperAppService.idl">Source file</a>
</div>

# nsIHelperAppLauncher #
<pre>  
A helper app launcher is a small object created to handle the launching  
of an external application.  
  
Note that cancelling the load via the nsICancelable interface will release  
the reference to the launcher dialog.  
  
</pre>
## Methods ##

### saveToDisk(aNewFileLocation, aRememberThisPreference) ###
<pre>  
Saves the final destination of the file. Does not actually perform the  
save.  
NOTE: This will release the reference to the  
nsIHelperAppLauncherDialog.  
  
</pre>
### launchWithApplication(aApplication, aRememberThisPreference) ###
<pre>  
Remembers that aApplication should be used to launch this content. Does  
not actually launch the application.  
NOTE: This will release the reference to the nsIHelperAppLauncherDialog.  
@param aApplication nsIFile corresponding to the location of the application to use.  
@param aRememberThisPreference TRUE if we should remember this choice.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aApplication</td>
<td>nsIFile corresponding to the location of the application to use.  
</td>
</tr>

<tr>
<td>aRememberThisPreference</td>
<td>TRUE if we should remember this choice.  
</td>
</tr>

</table>

### saveDestinationAvailable(aFile) ###
<pre>  
Callback invoked by nsIHelperAppLauncherDialog::promptForSaveToFileAsync  
after the user has chosen a file through the File Picker (or dismissed it).  
@param aFile The file that was chosen by the user (or null if dialog was dismissed).  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aFile</td>
<td>The file that was chosen by the user (or null if dialog was dismissed).  
</td>
</tr>

</table>

### setWebProgressListener(aWebProgressListener) ###
<pre>  
The following methods are used by the progress dialog to get or set  
information on the current helper app launcher download.  
This reference will be released when the download is finished (after the  
listener receives the STATE_STOP notification).  
  
</pre>
## Attributes ##

### MIMEInfo ###
<pre>  
The mime info object associated with the content type this helper app  
launcher is currently attempting to load  
  
</pre>
### source ###
<pre>  
The source uri  
  
</pre>
### suggestedFileName ###
<pre>  
The suggested name for this file  
  
</pre>
### targetFile ###
<pre>  
The file we are saving to  
  
</pre>
### targetFileIsExecutable ###
<pre>  
The executable-ness of the target file  
  
</pre>
### timeDownloadStarted ###
<pre>  
Time when the download started  
  
</pre>
### contentLength ###
<pre>  
The download content length, or -1 if the length is not available.  
  
</pre>