---
layout: default
---

# nsIApplicationCacheService #
  
The application cache service manages the set of application cache  
groups.  
  

## Methods ##

### buildGroupID(aManifestURL, aLoadContextInfo) ###
  
Create group string identifying cache group according the manifest  
URL and the given load context.  
  

### buildGroupIDForApp(aManifestURL, aAppID, aInBrowser) ###
  
Same as buildGroupID method, just doesn't require load context.  
  

### createApplicationCache(group) ###
  
Create a new, empty application cache for the given cache  
group.  
  

### createCustomApplicationCache(group, profileDir, quota) ###
  
Create a new, empty application cache for the given cache  
group residing in a custom directory with a custom quota.  
  
@param group  
   URL of the manifest  
@param directory  
   Actually a reference to a profile directory where to  
   create the OfflineCache sub-dir.  
@param quota  
   Optional override of the default quota.  
  

#### Parameters ####

<table>

<tr>
<td>group</td>
<td>   URL of the manifest  
</td>
</tr>

<tr>
<td>directory</td>
<td>   Actually a reference to a profile directory where to  
   create the OfflineCache sub-dir.  
</td>
</tr>

<tr>
<td>quota</td>
<td>   Optional override of the default quota.  
</td>
</tr>

</table>

### getApplicationCache(clientID) ###
  
Get an application cache object for the given client ID.  
  

### getActiveCache(group) ###
  
Get the currently active cache object for a cache group.  
  

### deactivateGroup(group) ###
  
Deactivate the currently-active cache object for a cache group.  
  

### discardByAppId(appID, discardOnlyBrowserEntries) ###
  
Deletes some or all of an application's cache entries.    
  
@param appId  
   The mozIApplication.localId of the application.  
  
@param discardOnlyBrowserEntries   
   If true, only entries marked as 'inBrowserElement' are deleted   
   (this is used by browser applications to delete user browsing   
   data/history.).  If false, *all* entries for the given appId are  
   deleted (this is used for application uninstallation).  
  

#### Parameters ####

<table>

<tr>
<td>appId</td>
<td>   The mozIApplication.localId of the application.  
</td>
</tr>

<tr>
<td>discardOnlyBrowserEntries</td>
<td>   If true, only entries marked as 'inBrowserElement' are deleted   
   (this is used by browser applications to delete user browsing   
   data/history.).  If false, *all* entries for the given appId are  
   deleted (this is used for application uninstallation).  
</td>
</tr>

</table>

### chooseApplicationCache(key, aLoadContextInfo) ###
  
Try to find the best application cache to serve a resource.  
  

### cacheOpportunistically(cache, key) ###
  
Flags the key as being opportunistically cached.  
  
This method should also propagate the entry to other  
application caches with the same opportunistic namespace, but  
this is not currently implemented.  
  
@param cache  
       The cache in which the entry is cached now.  
@param key  
       The cache entry key.  
  

#### Parameters ####

<table>

<tr>
<td>cache</td>
<td>       The cache in which the entry is cached now.  
</td>
</tr>

<tr>
<td>key</td>
<td>       The cache entry key.  
</td>
</tr>

</table>

### getGroups(count, groupIDs) ###
  
Get the list of application cache groups.  
  

### getGroupsTimeOrdered(count, groupIDs) ###
  
Get the list of application cache groups in the order of  
activating time.  
  
