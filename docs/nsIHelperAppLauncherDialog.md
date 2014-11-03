---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/exthandler/nsIHelperAppLauncherDialog.idl">Source file</a>
</div>

# nsIHelperAppLauncherDialog #
<pre>  
This interface is used to display a confirmation dialog before  
launching a "helper app" to handle content not handled by  
Mozilla.  
  
Usage:  Clients (of which there is one: the nsIExternalHelperAppService  
implementation in mozilla/uriloader/exthandler) create an instance of  
this interface (using the contract ID) and then call the show() method.  
  
The dialog is shown non-modally.  The implementation of the dialog  
will access methods of the nsIHelperAppLauncher passed in to show()  
in order to cause a "save to disk" or "open using" action.  
  
</pre>
## Methods ##

### show(aLauncher, aWindowContext, aReason) ###
<pre>  
Show confirmation dialog for launching application (or "save to  
disk") for content specified by aLauncher.  
  
@param aLauncher  
       A nsIHelperAppLauncher to be invoked when a file is selected.  
@param aWindowContext  
       Window associated with action.  
@param aReason  
       One of the constants from above. It indicates why the dialog is  
       shown. Implementors should treat unknown reasons like  
       REASON_CANTHANDLE.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aLauncher</td>
<td>       A nsIHelperAppLauncher to be invoked when a file is selected.  
</td>
</tr>

<tr>
<td>aWindowContext</td>
<td>       Window associated with action.  
</td>
</tr>

<tr>
<td>aReason</td>
<td>       One of the constants from above. It indicates why the dialog is  
       shown. Implementors should treat unknown reasons like  
       REASON_CANTHANDLE.  
</td>
</tr>

</table>

### promptForSaveToFile(aLauncher, aWindowContext, aDefaultFileName, aSuggestedFileExtension, aForcePrompt) ###
<pre>  
Invoke a save-to-file dialog instead of the full fledged helper app dialog.  
Returns the a nsIFile for the file name/location selected.  
  
@param aLauncher  
       A nsIHelperAppLauncher to be invoked when a file is selected.  
@param aWindowContext  
       Window associated with action.  
@param aDefaultFileName  
       Default file name to provide (can be null)  
@param aSuggestedFileExtension  
       Sugested file extension  
@param aForcePrompt  
       Set to true to force prompting the user for thet file  
       name/location, otherwise perferences may control if the user is  
       prompted.  
  
@throws NS_ERROR_NOT_AVAILABLE if the async version of this function  
                               should be used.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aLauncher</td>
<td>       A nsIHelperAppLauncher to be invoked when a file is selected.  
</td>
</tr>

<tr>
<td>aWindowContext</td>
<td>       Window associated with action.  
</td>
</tr>

<tr>
<td>aDefaultFileName</td>
<td>       Default file name to provide (can be null)  
</td>
</tr>

<tr>
<td>aSuggestedFileExtension</td>
<td>       Sugested file extension  
</td>
</tr>

<tr>
<td>aForcePrompt</td>
<td>       Set to true to force prompting the user for thet file  
       name/location, otherwise perferences may control if the user is  
       prompted.  
</td>
</tr>

</table>

### promptForSaveToFileAsync(aLauncher, aWindowContext, aDefaultFileName, aSuggestedFileExtension, aForcePrompt) ###
<pre>  
Async invoke a save-to-file dialog instead of the full fledged helper app  
dialog. When the file is chosen (or the dialog is closed), the callback  
in aLauncher (aLauncher.saveDestinationAvailable) is called with the  
selected file.  
  
@param aLauncher  
       A nsIHelperAppLauncher to be invoked when a file is selected.  
@param aWindowContext  
       Window associated with action.  
@param aDefaultFileName  
       Default file name to provide (can be null)  
@param aSuggestedFileExtension  
       Sugested file extension  
@param aForcePrompt  
       Set to true to force prompting the user for thet file  
       name/location, otherwise perferences may control if the user is  
       prompted.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aLauncher</td>
<td>       A nsIHelperAppLauncher to be invoked when a file is selected.  
</td>
</tr>

<tr>
<td>aWindowContext</td>
<td>       Window associated with action.  
</td>
</tr>

<tr>
<td>aDefaultFileName</td>
<td>       Default file name to provide (can be null)  
</td>
</tr>

<tr>
<td>aSuggestedFileExtension</td>
<td>       Sugested file extension  
</td>
</tr>

<tr>
<td>aForcePrompt</td>
<td>       Set to true to force prompting the user for thet file  
       name/location, otherwise perferences may control if the user is  
       prompted.  
</td>
</tr>

</table>

## Constants ##

### REASON_CANTHANDLE ###
<pre>  
This request is passed to the helper app dialog because Gecko can not  
handle content of this type.  
  
</pre>
### REASON_SERVERREQUEST ###
<pre>  
The server requested external handling.  
  
</pre>
### REASON_TYPESNIFFED ###
<pre>  
Gecko detected that the type sent by the server (e.g. text/plain) does  
not match the actual type.  
  
</pre>