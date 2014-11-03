---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/downloads/nsIDownloadManagerUI.idl">Source file</a>
</div>

# nsIDownloadManagerUI #

## Methods ##

### show(aWindowContext, aDownload, aReason, aUsePrivateUI) ###
<pre>  
Shows the Download Manager's UI to the user.  
  
@param [optional] aWindowContext  
       The parent window context to show the UI.  
@param [optional] aDownload  
       The download to be preselected upon opening.  
@param [optional] aReason  
       The reason to show the download manager's UI.  This defaults to  
       REASON_USER_INTERACTED, and should be one of the previously listed  
       constants.  
@param [optional] aUsePrivateUI  
       Pass true as this argument to hint to the implementation that it  
       should only display private downloads in the UI, if possible.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>[optional]</td>
<td>aWindowContext  
       The parent window context to show the UI.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aDownload  
       The download to be preselected upon opening.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aReason  
       The reason to show the download manager's UI.  This defaults to  
       REASON_USER_INTERACTED, and should be one of the previously listed  
       constants.  
</td>
</tr>

<tr>
<td>[optional]</td>
<td>aUsePrivateUI  
       Pass true as this argument to hint to the implementation that it  
       should only display private downloads in the UI, if possible.  
</td>
</tr>

</table>

### getAttention() ###
<pre>  
Brings attention to the UI if it is already visible  
  
@throws NS_ERROR_UNEXPECTED if the UI is not visible.  
  
</pre>
## Attributes ##

### visible ###
<pre>  
Indicates if the UI is visible or not.  
  
</pre>
## Constants ##

### REASON_USER_INTERACTED ###
<pre>  
The reason that should be passed when the user requests to show the  
download manager's UI.  
  
</pre>
### REASON_NEW_DOWNLOAD ###
<pre>  
The reason that should be passed to the show method when we are displaying  
the UI because a new download is being added to it.  
  
</pre>