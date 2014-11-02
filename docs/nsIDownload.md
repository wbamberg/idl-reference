---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/downloads/nsIDownload.idl">Source file</a>
</div>
# nsIDownload #
  
Represents a download object.  
  
@note This object is no longer updated once it enters a completed state.  
      Completed states are the following:    
      nsIDownloadManager::DOWNLOAD_FINISHED    
      nsIDownloadManager::DOWNLOAD_FAILED    
      nsIDownloadManager::DOWNLOAD_CANCELED   
      nsIDownloadManager::DOWNLOAD_BLOCKED_PARENTAL   
      nsIDownloadManager::DOWNLOAD_DIRTY   
      nsIDownloadManager::DOWNLOAD_BLOCKED_POLICY   
  

## Methods ##

### cancel() ###
  
Cancel this download if it's currently in progress.  
  

### pause() ###
  
Pause this download if it is in progress.  
  
@throws NS_ERROR_UNEXPECTED if it cannot be paused.  
  

### resume() ###
  
Resume this download if it is paused.  
  
@throws NS_ERROR_UNEXPECTED if it cannot be resumed or is not paused.  
  

### remove() ###
  
Instruct the download manager to remove this download. Whereas  
cancel simply cancels the transfer, but retains information about it,  
remove removes all knowledge of it.  
  
@see nsIDownloadManager.removeDownload for more detail  
@throws NS_ERROR_FAILURE if the download is active.  
  

### retry() ###
  
Instruct the download manager to retry this failed download  
@throws NS_ERROR_NOT_AVAILABLE if the download is not known.  
@throws NS_ERROR_FAILURE if the download is not in the following states:  
        nsIDownloadManager::DOWNLOAD_CANCELED  
        nsIDownloadManager::DOWNLOAD_FAILED  
  

## Attributes ##

### targetFile ###
  
The target of a download is always a file on the local file system.  
  

### percentComplete ###
  
The percentage of transfer completed.  
If the file size is unknown it'll be -1 here.  
  

### amountTransferred ###
  
The amount of bytes downloaded so far.  
  

### size ###
  
The size of file in bytes.  
Unknown size is represented by -1.  
  

### source ###
  
The source of the transfer.  
  

### target ###
  
The target of the transfer.  
  

### cancelable ###
  
Object that can be used to cancel the download.  
Will be null after the download is finished.  
  

### displayName ###
  
The user-readable description of the transfer.  
  

### startTime ###
  
The time a transfer was started.  
  

### speed ###
  
The speed of the transfer in bytes/sec.  
  

### MIMEInfo ###
  
Optional. If set, it will contain the target's relevant MIME information.  
This includes its MIME Type, helper app, and whether that helper should be  
executed.  
  

### id ###
  
The id of the download that is stored in the database - not globally unique.  
For example, a private download and a public one might have identical ids.  
Can only be safely used for direct database manipulation in the database that  
contains this download. Use the guid property instead for safe, database-agnostic  
searching and manipulation.  
  
@deprecated  
  

### guid ###
  
The guid of the download that is stored in the database.  
Has the form of twelve alphanumeric characters.  
  

### state ###
  
The state of the download.  
@see nsIDownloadManager and nsIXPInstallManagerUI  
  

### referrer ###
  
The referrer uri of the download.  This is only valid for HTTP downloads,  
and can be null.  
  

### resumable ###
  
Indicates if the download can be resumed after being paused or not.  This  
is only the case if the download is over HTTP/1.1 or FTP and if the  
server supports it.  
  

### isPrivate ###
  
Indicates if the download was initiated from a context marked as private,  
controlling whether it should be stored in a permanent manner or not.  
  
