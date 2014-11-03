---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/prefetch/nsIOfflineCacheUpdate.idl">Source file</a>
</div>

# nsIOfflineCacheUpdate #
<code>  
An nsIOfflineCacheUpdate is used to update an application's offline  
resources.  
  
It can be used to perform partial or complete updates.  
  
One update object will be updating at a time.  The active object will  
load its items one by one, sending itemCompleted() to any registered  
observers.  
  
</code>
## Methods ##

### init(aManifestURI, aDocumentURI, aDocument, aCustomProfileDir, aAppId, aInBrowser) ###
<code>  
Initialize the update.  
  
@param aManifestURI  
       The manifest URI to be checked.  
@param aDocumentURI  
       The page that is requesting the update.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManifestURI</td>
<td>       The manifest URI to be checked.  
</td>
</tr>

<tr>
<td>aDocumentURI</td>
<td>       The page that is requesting the update.  
</td>
</tr>

</table>

### initPartial(aManifestURI, aClientID, aDocumentURI) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManifestURI</td>
<td>       The manifest URI of the related cache.  
</td>
</tr>

<tr>
<td>aClientID</td>
<td>       Client  ID of the cache to store resource to. This ClientID  
       must be ID of cache in the cache group identified by  
       the manifest URI passed in the first parameter.  
</td>
</tr>

<tr>
<td>aDocumentURI</td>
<td>       The page that is requesting the update. May be null   
       when this information is unknown.  
</td>
</tr>

</table>

### initForUpdateCheck(aManifestURI, aAppID, aInBrowser, aObserver) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>aManifestURI</td>
<td>       The manifest URI of the related cache.  
</td>
</tr>

<tr>
<td>aAppID</td>
<td>       Local ID of an app (optional) to check the cache update for.  
</td>
</tr>

<tr>
<td>aInBrowser</td>
<td>       Whether to check for a cache populated from browser element.  
</td>
</tr>

<tr>
<td>aObserver</td>
<td>       nsIObserver implementation that receives the result.  
       When aTopic == "offline-cache-update-available" there is an update to  
       to download. Update of the app cache will lead to a new version  
       download.  
       When aTopic == "offline-cache-update-unavailable" then there is no  
       update available (the manifest has not changed on the server).  
</td>
</tr>

</table>

### addDynamicURI(aURI) ###
<code>  
Add a dynamic URI to the offline cache as part of the update.  
  
@param aURI  
       The URI to add.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI to add.  
</td>
</tr>

</table>

### schedule() ###
<code>  
Add the update to the offline update queue.  An offline-cache-update-added  
event will be sent to the observer service.  
  
</code>
### addObserver(aObserver, aHoldWeak) ###
<code>  
Observe loads that are added to the update.  
  
@param aObserver  
       object that notifications will be sent to.  
@param aHoldWeak  
       TRUE if you want the update to hold a weak reference to the  
       observer, FALSE for a strong reference.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>       object that notifications will be sent to.  
</td>
</tr>

<tr>
<td>aHoldWeak</td>
<td>       TRUE if you want the update to hold a weak reference to the  
       observer, FALSE for a strong reference.  
</td>
</tr>

</table>

### removeObserver(aObserver) ###
<code>  
Remove an observer from the update.  
  
@param aObserver  
       the observer to remove.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>       the observer to remove.  
</td>
</tr>

</table>

### cancel() ###
<code>  
Cancel the update when still in progress. This stops all running resource  
downloads and discards the downloaded cache version. Throws when update  
has already finished and made the new cache version active.  
  
</code>
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
  
