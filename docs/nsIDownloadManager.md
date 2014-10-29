---
layout: default
---

# nsIDownloadManager #

## DOWNLOAD_TYPE_DOWNLOAD ##

Download type for generic file download.


## DOWNLOAD_NOTSTARTED ##

Download state for uninitialized download object.


## DOWNLOAD_DOWNLOADING ##

Download is currently transferring data.


## DOWNLOAD_FINISHED ##

Download completed including any processing of the target
file.  (completed)


## DOWNLOAD_FAILED ##

Transfer failed due to error. (completed)


## DOWNLOAD_CANCELED ##

Download was canceled by the user. (completed)


## DOWNLOAD_PAUSED ##

Transfer was paused by the user.


## DOWNLOAD_QUEUED ##

Download is active but data has not yet been received.


## DOWNLOAD_BLOCKED_PARENTAL ##

Transfer request was blocked by parental controls proxies. (completed)


## DOWNLOAD_SCANNING ##

Transferred download is being scanned by virus scanners.


## DOWNLOAD_DIRTY ##

A virus was detected in the download. The target will most likely
no longer exist. (completed)


## DOWNLOAD_BLOCKED_POLICY ##

Win specific: Request was blocked by zone policy settings.
(see bug #416683) (completed)


## addDownload ##

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


## getDownload ##

Retrieves a download managed by the download manager.  This can be one that
is in progress, or one that has completed in the past and is stored in the
database.

@param aID The unique ID of the download.
@return The download with the specified ID.
@throws NS_ERROR_NOT_AVAILABLE if the download is not in the database.


## getDownloadByGUID ##

Retrieves a download managed by the download manager.  This can be one that
is in progress, or one that has completed in the past and is stored in the
database.  The result of this method is returned via an asynchronous callback,
the parameter of which will be an nsIDownload object, or null if none exists
with the provided GUID.

@param aGUID The unique GUID of the download.
@param aCallback The callback to invoke with the result of the search.


## cancelDownload ##

Cancels the download with the specified ID if it's currently in-progress.
This calls cancel(NS_BINDING_ABORTED) on the nsICancelable provided by the
download.

@param aID The unique ID of the download.
@throws NS_ERROR_FAILURE if the download is not in-progress.


## removeDownload ##

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


## removeDownloadsByTimeframe ##

Removes all inactive downloads that were started inclusively within the
specified time frame.

@param aBeginTime
       The start time to remove downloads by in microseconds.
@param aEndTime
       The end time to remove downloads by in microseconds.


## pauseDownload ##

Pause the specified download.

@param aID The unique ID of the download.
@throws NS_ERROR_FAILURE if the download is not in-progress.


## resumeDownload ##

Resume the specified download.

@param aID The unique ID of the download.
@throws NS_ERROR_FAILURE if the download is not in-progress.


## retryDownload ##

Retries a failed download.

@param aID The unique ID of the download.
@throws NS_ERROR_NOT_AVAILALE if the download id is not known.
@throws NS_ERROR_FAILURE if the download is not in the following states:
          nsIDownloadManager::DOWNLOAD_CANCELED
          nsIDownloadManager::DOWNLOAD_FAILED


## DBConnection ##

The database connection to the downloads database.


## privateDBConnection ##

## canCleanUp ##
 
Whether or not there are downloads that can be cleaned up (removed)
i.e. downloads that have completed, have failed or have been canceled.
In global private browsing mode, this reports the status of the relevant
private or public downloads. In per-window mode, it only reports for
public ones.


## canCleanUpPrivate ##
 
Whether or not there are private downloads that can be cleaned up (removed)
i.e. downloads that have completed, have failed or have been canceled.


## cleanUp ##
 
Removes completed, failed, and canceled downloads from the list.
In global private browsing mode, this operates on the relevant
private or public downloads. In per-window mode, it only operates
on public ones.

Also notifies observers of the "download-manager-remove-download-gui"
and "download-manager-remove-download" topics with a null subject to
allow any DM consumers to react to the removals.


## cleanUpPrivate ##
 
Removes completed, failed, and canceled downloads from the list
of private downloads.

Also notifies observers of the "download-manager-remove-download-gui"
and "download-manager-remove-download" topics with a null subject to
allow any DM consumers to react to the removals.


## activeDownloadCount ##
 
The number of files currently being downloaded.

In global private browsing mode, this reports the status of the relevant
private or public downloads. In per-window mode, it only reports public
ones.


## activePrivateDownloadCount ##
 
The number of private files currently being downloaded.


## activeDownloads ##

An enumeration of active nsIDownloads

In global private browsing mode, this reports the status of the relevant
private or public downloads. In per-window mode, it only reports public
ones.


## activePrivateDownloads ##

An enumeration of active private nsIDownloads


## addListener ##

Adds a listener to the download manager. It is expected that this
listener will only access downloads via their deprecated integer id attribute,
and when global private browsing compatibility mode is disabled, this listener
will receive no notifications for downloads marked private.


## addPrivacyAwareListener ##

Adds a listener to the download manager. This listener must be able to
understand and use the guid attribute of downloads for all interactions
with the download manager.


## removeListener ##

Removes a listener from the download manager.


## defaultDownloadsDirectory ##

Returns the platform default downloads directory.


## userDownloadsDirectory ##

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

