---
layout: default
---

# nsIApplicationUpdateService #

An interface describing a global application service that handles performing
background update checks and provides utilities for selecting and
downloading update patches.


## checkForBackgroundUpdates ##

Checks for available updates in the background using the listener provided
by the application update service for background checks.


## backgroundChecker ##

The Update Checker used for background update checking.


## selectUpdate ##

Selects the best update to install from a list of available updates.
@param   updates
         An array of updates that are available
@param   updateCount
         The length of the |updates| array


## addDownloadListener ##

Adds a listener that receives progress and state information about the
update that is currently being downloaded, e.g. to update a user
interface.
@param   listener
         An object implementing nsIRequestObserver and optionally
         nsIProgressEventSink that is to be notified of state and
         progress information as the update is downloaded.


## removeDownloadListener ##

Removes a listener that is receiving progress and state information
about the update that is currently being downloaded.
@param   listener
         The listener object to remove.


## downloadUpdate ##




## applyOsUpdate ##

Apply the OS update which has been downloaded and staged as applied.
@param   update 
         The update has been downloaded and staged as applied.
@throws  if the update object is not an OS update.


## getUpdatesDirectory ##

Get the Active Updates directory
@returns An nsIFile for the active updates directory.


## pauseDownload ##

Pauses the active update download process


## isDownloading ##

Whether or not there is an download happening at the moment.


## canCheckForUpdates ##

Whether or not the Update Service can check for updates. This is a function
of whether or not application update is disabled by the application and the
platform the application is running on.


## canApplyUpdates ##

Whether or not the Update Service can download and install updates.
On Windows, this is a function of whether or not the maintenance service
is installed and enabled. On other systems, and as a fallback on Windows,
this depends on whether the current user has write access to the install
directory.


## isOtherInstanceHandlingUpdates ##

Whether or not a different instance is handling updates of this
installation.  This currently only ever returns true on Windows
when 2 instances of an application are open or when both the Metro
and Desktop browsers are open.  Only one of the instances will actually
handle updates for the installation.


## canStageUpdates ##

Whether the Update Service is able to stage updates.

