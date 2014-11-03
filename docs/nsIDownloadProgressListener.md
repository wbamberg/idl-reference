---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/downloads/nsIDownloadProgressListener.idl">Source file</a>
</div>

# nsIDownloadProgressListener #

## Methods ##

### onDownloadStateChange(aState, aDownload) ###
  
Dispatched whenever the state of the download changes.  
  
  

#### Parameters ####

<table>

<tr>
<td>aState</td>
<td>The previous download sate.  
</td>
</tr>

<tr>
<td>aDownload</td>
<td>The download object.  
@see nsIDownloadManager for download states.  
</td>
</tr>

</table>

### onStateChange(aWebProgress, aRequest, aStateFlags, aStatus, aDownload) ###

### onProgressChange(aWebProgress, aRequest, aCurSelfProgress, aMaxSelfProgress, aCurTotalProgress, aMaxTotalProgress, aDownload) ###

### onSecurityChange(aWebProgress, aRequest, aState, aDownload) ###

## Attributes ##

### document ###
  
document  
The document of the download manager frontend.  
  
