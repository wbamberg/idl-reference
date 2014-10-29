---
layout: default
---

# nsIQuotaManager #

## getUsageForURI ##

Schedules an asynchronous callback that will return the total amount of
disk space being used by storages for the given origin.

@param aURI
       The URI whose usage is being queried.
@param aCallback
       The callback that will be called when the usage is available.


## clear ##

Removes all storages. The files may not be deleted immediately depending
on prohibitive concurrent operations.
Be careful, this removes *all* the data that has ever been stored!

If the dom.quotaManager.testing preference is not true the call will be
a no-op.


## clearStoragesForURI ##

Removes all storages stored for the given URI. The files may not be
deleted immediately depending on prohibitive concurrent operations.

@param aURI
       The URI whose storages are to be cleared.


## reset ##

Resets quota and storage management. This can be used to force
reinitialization of the temp storage, for example when the pref for
overriding the temp storage limit has changed.
Be carefull, this invalidates all live storages!

If the dom.quotaManager.testing preference is not true the call will be
a no-op.

