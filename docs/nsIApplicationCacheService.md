---
layout: default
---

# nsIApplicationCacheService #

The application cache service manages the set of application cache
groups.


## buildGroupID ##

Create group string identifying cache group according the manifest
URL and the given load context.


## buildGroupIDForApp ##

Same as buildGroupID method, just doesn't require load context.


## createApplicationCache ##

Create a new, empty application cache for the given cache
group.


## createCustomApplicationCache ##

Create a new, empty application cache for the given cache
group residing in a custom directory with a custom quota.

@param group
   URL of the manifest
@param directory
   Actually a reference to a profile directory where to
   create the OfflineCache sub-dir.
@param quota
   Optional override of the default quota.


## getApplicationCache ##

Get an application cache object for the given client ID.


## getActiveCache ##

Get the currently active cache object for a cache group.


## deactivateGroup ##

Deactivate the currently-active cache object for a cache group.


## discardByAppId ##

Deletes some or all of an application's cache entries.  

@param appId
   The mozIApplication.localId of the application.

@param discardOnlyBrowserEntries 
   If true, only entries marked as 'inBrowserElement' are deleted 
   (this is used by browser applications to delete user browsing 
   data/history.).  If false, *all* entries for the given appId are
   deleted (this is used for application uninstallation).


## chooseApplicationCache ##

Try to find the best application cache to serve a resource.


## cacheOpportunistically ##

Flags the key as being opportunistically cached.

This method should also propagate the entry to other
application caches with the same opportunistic namespace, but
this is not currently implemented.

@param cache
       The cache in which the entry is cached now.
@param key
       The cache entry key.


## getGroups ##

Get the list of application cache groups.


## getGroupsTimeOrdered ##

Get the list of application cache groups in the order of
activating time.

