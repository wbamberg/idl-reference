---
layout: default
---

# nsIOfflineCacheUpdate #

An nsIOfflineCacheUpdate is used to update an application's offline
resources.

It can be used to perform partial or complete updates.

One update object will be updating at a time.  The active object will
load its items one by one, sending itemCompleted() to any registered
observers.


## Methods ##

### init ###

Initialize the update.

@param aManifestURI
       The manifest URI to be checked.
@param aDocumentURI
       The page that is requesting the update.


### initPartial ###

Initialize the update for partial processing. 

@param aManifestURI
       The manifest URI of the related cache.
@param aClientID
       Client  ID of the cache to store resource to. This ClientID
       must be ID of cache in the cache group identified by
       the manifest URI passed in the first parameter.
@param aDocumentURI
       The page that is requesting the update. May be null 
       when this information is unknown.


### initForUpdateCheck ###

Initialize the update to only check whether there is an update
to the manifest available (if it has actually changed on the server).

@param aManifestURI
       The manifest URI of the related cache.
@param aAppID
       Local ID of an app (optional) to check the cache update for.
@param aInBrowser
       Whether to check for a cache populated from browser element.
@param aObserver
       nsIObserver implementation that receives the result.
       When aTopic == "offline-cache-update-available" there is an update to
       to download. Update of the app cache will lead to a new version
       download.
       When aTopic == "offline-cache-update-unavailable" then there is no
       update available (the manifest has not changed on the server).


### addDynamicURI ###

Add a dynamic URI to the offline cache as part of the update.

@param aURI
       The URI to add.


### schedule ###

Add the update to the offline update queue.  An offline-cache-update-added
event will be sent to the observer service.


### addObserver ###

Observe loads that are added to the update.

@param aObserver
       object that notifications will be sent to.
@param aHoldWeak
       TRUE if you want the update to hold a weak reference to the
       observer, FALSE for a strong reference.


### removeObserver ###

Remove an observer from the update.

@param aObserver
       the observer to remove.


### cancel ###

Cancel the update when still in progress. This stops all running resource
downloads and discards the downloaded cache version. Throws when update
has already finished and made the new cache version active.


## Attributes ##

### status ###

Fetch the status of the running update.  This will return a value
defined in nsIDOMOfflineResourceList.


### partial ###

TRUE if the update is being used to add specific resources.
FALSE if the complete cache update process is happening.


### isUpgrade ###

TRUE if this is an upgrade attempt, FALSE if it is a new cache
attempt.


### updateDomain ###

The domain being updated, and the domain that will own any URIs added
with this update.


### manifestURI ###

The manifest for the offline application being updated.


### succeeded ###

TRUE if the cache update completed successfully.


### byteProgress ###

Return the number of bytes downloaded so far

