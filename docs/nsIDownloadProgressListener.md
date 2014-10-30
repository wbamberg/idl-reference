---
layout: default
---

# nsIDownloadProgressListener #

## Methods ##

### onDownloadStateChange(aState, aDownload) ###
  
Dispatched whenever the state of the download changes.  
  
@param aState The previous download sate.  
@param aDownload The download object.  
@see nsIDownloadManager for download states.  
  

### onStateChange(aWebProgress, aRequest, aStateFlags, aStatus, aDownload) ###

### onProgressChange(aWebProgress, aRequest, aCurSelfProgress, aMaxSelfProgress, aCurTotalProgress, aMaxTotalProgress, aDownload) ###

### onSecurityChange(aWebProgress, aRequest, aState, aDownload) ###

## Attributes ##

### document ###
  
document  
The document of the download manager frontend.  
  
