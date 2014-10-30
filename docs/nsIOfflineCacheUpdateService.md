---
layout: default
---

# nsIOfflineCacheUpdateService #

## Methods ##

### getUpdate(index) ###

### scheduleUpdate(aManifestURI, aDocumentURI, aWindow) ###
  
Schedule a cache update for a given offline manifest.  If an  
existing update is scheduled or running, that update will be returned.  
Otherwise a new update will be scheduled.  
  

### scheduleAppUpdate(aManifestURI, aDocumentURI, aAppID, aInBrowser, aProfileDir) ###
  
Schedule a cache update for a given offline manifest using app cache  
bound to the given appID+inBrowser flag.  If an existing update is  
scheduled or running, that update will be returned. Otherwise a new  
update will be scheduled.  
  

### scheduleOnDocumentStop(aManifestURI, aDocumentURI, aDocument) ###
  
Schedule a cache update for a manifest when the document finishes  
loading.  
  

### checkForUpdate(aManifestURI, aAppID, aInBrowser, aObserver) ###
  
Schedule a check to see if an update is available.  
  
This will not update or make any changes to the appcache.  
It only notifies the observer to indicate whether the manifest has  
changed on the server (or not): a changed manifest means that an  
update is available.  
  
For arguments see nsIOfflineCacheUpdate.initForUpdateCheck() method  
description.  
  

### offlineAppAllowed(aPrincipal, aPrefBranch) ###
  
Checks whether a principal should have access to the offline  
cache.  
@param aPrincipal  
       The principal to check.  
@param aPrefBranch  
       The pref branch to use to check the  
       offline-apps.allow_by_default pref.  If not specified,  
       the pref service will be used.  
  

### offlineAppAllowedForURI(aURI, aPrefBranch) ###
  
Checks whether a document at the given URI should have access  
to the offline cache.  
@param aURI  
       The URI to check  
@param aPrefBranch  
       The pref branch to use to check the  
       offline-apps.allow_by_default pref.  If not specified,  
       the pref service will be used.  
  

### allowOfflineApp(aWindow, aPrincipal) ###
  
Sets the "offline-app" permission for the principal.  
In the single process model calls directly on permission manager.  
In the multi process model dispatches to the parent process.  
  

## Attributes ##

### numUpdates ###
  
Access to the list of cache updates that have been scheduled.  
  

## Constants ##

### ALLOW_NO_WARN ###
  
Constants for the offline-app permission.  
  
XXX: This isn't a great place for this, but it's really the only  
private offline-app-related interface  
  
  
Allow the domain to use offline APIs, and don't warn about excessive  
usage.  
  
