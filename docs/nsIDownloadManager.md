---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/downloads/nsIDownloadManager.idl">Source file</a>
</div>

# nsIDownloadManager #

## Methods ##

### addDownload(aDownloadType, aSource, aTarget, aDisplayName, aMIMEInfo, aStartTime, aTempFile, aCancelable, aIsPrivate) ###
<pre>  
Creates an nsIDownload and adds it to be managed by the download manager.  
  
@param aSource The source URI of the transfer. Must not be null.  
  
@param aTarget The target URI of the transfer. Must not be null.  
  
@param aDisplayName The user-readable description of the transfer.  
                    Can be empty.  
  
@param aMIMEInfo The MIME info associated with the target,  
                 including MIME type and helper app when appropriate.  
                 This parameter is optional.  
  
@param startTime Time when the download started  
  
@param aTempFile The location of a temporary file; i.e. a file in which  
                 the received data will be stored, but which is not  
                 equal to the target file. (will be moved to the real  
                 target by the DownloadManager, when the download is  
                 finished). This will be null for all callers except for  
                 nsExternalHelperAppHandler. Addons should generally pass  
                 null for aTempFile. This will be moved to the real target  
                 by the download manager when the download is finished,  
                 and the action indicated by aMIMEInfo will be executed.  
  
@param aCancelable An object that can be used to abort the download.  
                   Must not be null.  
  
@param aIsPrivate Used to determine the privacy status of the new download.  
                  If true, the download is stored in a manner that leaves  
                  no permanent trace outside of the current private session.  
  
@return The newly created download item with the passed-in properties.  
  
@note This does not actually start a download.  If you want to add and  
      start a download, you need to create an nsIWebBrowserPersist, pass it  
      as the aCancelable object, call this method, set the progressListener  
      as the returned download object, then call saveURI.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aSource</td>
<td>The source URI of the transfer. Must not be null.  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>The target URI of the transfer. Must not be null.  
</td>
</tr>

<tr>
<td>aDisplayName</td>
<td>The user-readable description of the transfer.  
                    Can be empty.  
</td>
</tr>

<tr>
<td>aMIMEInfo</td>
<td>The MIME info associated with the target,  
                 including MIME type and helper app when appropriate.  
                 This parameter is optional.  
</td>
</tr>

<tr>
<td>startTime</td>
<td>Time when the download started  
</td>
</tr>

<tr>
<td>aTempFile</td>
<td>The location of a temporary file; i.e. a file in which  
                 the received data will be stored, but which is not  
                 equal to the target file. (will be moved to the real  
                 target by the DownloadManager, when the download is  
                 finished). This will be null for all callers except for  
                 nsExternalHelperAppHandler. Addons should generally pass  
                 null for aTempFile. This will be moved to the real target  
                 by the download manager when the download is finished,  
                 and the action indicated by aMIMEInfo will be executed.  
</td>
</tr>

<tr>
<td>aCancelable</td>
<td>An object that can be used to abort the download.  
                   Must not be null.  
</td>
</tr>

<tr>
<td>aIsPrivate</td>
<td>Used to determine the privacy status of the new download.  
                  If true, the download is stored in a manner that leaves  
                  no permanent trace outside of the current private session.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The newly created download item with the passed-in properties.  
</td>
</tr>

</table>

### getDownload(aID) ###
<pre>  
Retrieves a download managed by the download manager.  This can be one that  
is in progress, or one that has completed in the past and is stored in the  
database.  
  
@param aID The unique ID of the download.  
@return The download with the specified ID.  
@throws NS_ERROR_NOT_AVAILABLE if the download is not in the database.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aID</td>
<td>The unique ID of the download.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The download with the specified ID.  
@throws NS_ERROR_NOT_AVAILABLE if the download is not in the database.  
</td>
</tr>

</table>

### getDownloadByGUID(aGUID, aCallback) ###
<pre>  
Retrieves a download managed by the download manager.  This can be one that  
is in progress, or one that has completed in the past and is stored in the  
database.  The result of this method is returned via an asynchronous callback,  
the parameter of which will be an nsIDownload object, or null if none exists  
with the provided GUID.  
  
@param aGUID The unique GUID of the download.  
@param aCallback The callback to invoke with the result of the search.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aGUID</td>
<td>The unique GUID of the download.  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>The callback to invoke with the result of the search.  
</td>
</tr>

</table>

### cancelDownload(aID) ###
<pre>  
Cancels the download with the specified ID if it's currently in-progress.  
This calls cancel(NS_BINDING_ABORTED) on the nsICancelable provided by the  
download.  
  
@param aID The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is not in-progress.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aID</td>
<td>The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is not in-progress.  
</td>
</tr>

</table>

### removeDownload(aID) ###
<pre>  
Removes the download with the specified id if it's not currently  
in-progress.  Whereas cancelDownload simply cancels the transfer, but  
retains information about it, removeDownload removes all knowledge of it.  
  
Also notifies observers of the "download-manager-remove-download-guid"  
topic with the download guid as the subject to allow any DM consumers to  
react to the removal.  
  
Also may notify observers of the "download-manager-remove-download" topic  
with the download id as the subject, if the download removed is public  
or if global private browsing mode is in use. This notification is deprecated;  
the guid notification should be relied upon instead.  
  
@param aID The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is active.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aID</td>
<td>The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is active.  
</td>
</tr>

</table>

### removeDownloadsByTimeframe(aBeginTime, aEndTime) ###
<pre>  
Removes all inactive downloads that were started inclusively within the  
specified time frame.  
  
@param aBeginTime  
       The start time to remove downloads by in microseconds.  
@param aEndTime  
       The end time to remove downloads by in microseconds.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aBeginTime</td>
<td>       The start time to remove downloads by in microseconds.  
</td>
</tr>

<tr>
<td>aEndTime</td>
<td>       The end time to remove downloads by in microseconds.  
</td>
</tr>

</table>

### pauseDownload(aID) ###
<pre>  
Pause the specified download.  
  
@param aID The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is not in-progress.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aID</td>
<td>The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is not in-progress.  
</td>
</tr>

</table>

### resumeDownload(aID) ###
<pre>  
Resume the specified download.  
  
@param aID The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is not in-progress.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aID</td>
<td>The unique ID of the download.  
@throws NS_ERROR_FAILURE if the download is not in-progress.  
</td>
</tr>

</table>

### retryDownload(aID) ###
<pre>  
Retries a failed download.  
  
@param aID The unique ID of the download.  
@throws NS_ERROR_NOT_AVAILALE if the download id is not known.  
@throws NS_ERROR_FAILURE if the download is not in the following states:  
          nsIDownloadManager::DOWNLOAD_CANCELED  
          nsIDownloadManager::DOWNLOAD_FAILED  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aID</td>
<td>The unique ID of the download.  
@throws NS_ERROR_NOT_AVAILALE if the download id is not known.  
@throws NS_ERROR_FAILURE if the download is not in the following states:  
          nsIDownloadManager::DOWNLOAD_CANCELED  
          nsIDownloadManager::DOWNLOAD_FAILED  
</td>
</tr>

</table>

### cleanUp() ###
<pre>   
Removes completed, failed, and canceled downloads from the list.  
In global private browsing mode, this operates on the relevant  
private or public downloads. In per-window mode, it only operates  
on public ones.  
  
Also notifies observers of the "download-manager-remove-download-gui"  
and "download-manager-remove-download" topics with a null subject to  
allow any DM consumers to react to the removals.  
  
</pre>
### cleanUpPrivate() ###
<pre>   
Removes completed, failed, and canceled downloads from the list  
of private downloads.  
  
Also notifies observers of the "download-manager-remove-download-gui"  
and "download-manager-remove-download" topics with a null subject to  
allow any DM consumers to react to the removals.  
  
</pre>
### addListener(aListener) ###
<pre>  
Adds a listener to the download manager. It is expected that this  
listener will only access downloads via their deprecated integer id attribute,  
and when global private browsing compatibility mode is disabled, this listener  
will receive no notifications for downloads marked private.  
  
</pre>
### addPrivacyAwareListener(aListener) ###
<pre>  
Adds a listener to the download manager. This listener must be able to  
understand and use the guid attribute of downloads for all interactions  
with the download manager.  
  
</pre>
### removeListener(aListener) ###
<pre>  
Removes a listener from the download manager.  
  
</pre>
## Attributes ##

### DBConnection ###
<pre>  
The database connection to the downloads database.  
  
</pre>
### privateDBConnection ###

### canCleanUp ###
<pre>   
Whether or not there are downloads that can be cleaned up (removed)  
i.e. downloads that have completed, have failed or have been canceled.  
In global private browsing mode, this reports the status of the relevant  
private or public downloads. In per-window mode, it only reports for  
public ones.  
  
</pre>
### canCleanUpPrivate ###
<pre>   
Whether or not there are private downloads that can be cleaned up (removed)  
i.e. downloads that have completed, have failed or have been canceled.  
  
</pre>
### activeDownloadCount ###
<pre>   
The number of files currently being downloaded.  
  
In global private browsing mode, this reports the status of the relevant  
private or public downloads. In per-window mode, it only reports public  
ones.  
  
</pre>
### activePrivateDownloadCount ###
<pre>   
The number of private files currently being downloaded.  
  
</pre>
### activeDownloads ###
<pre>  
An enumeration of active nsIDownloads  
  
In global private browsing mode, this reports the status of the relevant  
private or public downloads. In per-window mode, it only reports public  
ones.  
  
</pre>
### activePrivateDownloads ###
<pre>  
An enumeration of active private nsIDownloads  
  
</pre>
### defaultDownloadsDirectory ###
<pre>  
Returns the platform default downloads directory.  
  
</pre>
### userDownloadsDirectory ###
<pre>  
Returns the user configured downloads directory.   
The path is dependent on two user configurable prefs  
set in preferences:  
  
browser.download.folderList  
  Indicates the location users wish to save downloaded   
  files too.    
  Values:   
    0 - The desktop is the default download location.   
    1 - The system's downloads folder is the default download location.   
    2 - The default download location is elsewhere as specified in    
        browser.download.dir. If invalid, userDownloadsDirectory  
        will fallback on defaultDownloadsDirectory.  
  
browser.download.dir -   
  A local path the user may have selected at some point   
  where downloaded files are saved. The use of which is  
  enabled when folderList equals 2.   
  
</pre>
## Constants ##

### DOWNLOAD_TYPE_DOWNLOAD ###
<pre>  
Download type for generic file download.  
  
</pre>
### DOWNLOAD_NOTSTARTED ###
<pre>  
Download state for uninitialized download object.  
  
</pre>
### DOWNLOAD_DOWNLOADING ###
<pre>  
Download is currently transferring data.  
  
</pre>
### DOWNLOAD_FINISHED ###
<pre>  
Download completed including any processing of the target  
file.  (completed)  
  
</pre>
### DOWNLOAD_FAILED ###
<pre>  
Transfer failed due to error. (completed)  
  
</pre>
### DOWNLOAD_CANCELED ###
<pre>  
Download was canceled by the user. (completed)  
  
</pre>
### DOWNLOAD_PAUSED ###
<pre>  
Transfer was paused by the user.  
  
</pre>
### DOWNLOAD_QUEUED ###
<pre>  
Download is active but data has not yet been received.  
  
</pre>
### DOWNLOAD_BLOCKED_PARENTAL ###
<pre>  
Transfer request was blocked by parental controls proxies. (completed)  
  
</pre>
### DOWNLOAD_SCANNING ###
<pre>  
Transferred download is being scanned by virus scanners.  
  
</pre>
### DOWNLOAD_DIRTY ###
<pre>  
A virus was detected in the download. The target will most likely  
no longer exist. (completed)  
  
</pre>
### DOWNLOAD_BLOCKED_POLICY ###
<pre>  
Win specific: Request was blocked by zone policy settings.  
(see bug #416683) (completed)  
  
</pre>