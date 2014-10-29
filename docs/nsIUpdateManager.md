---
layout: default
---

# nsIUpdateManager #

An interface describing a global application service that maintains a list
of updates previously performed as well as the current active update.


## getUpdateAt ##

Gets the update at the specified index
@param   index
         The index within the updates array
@returns The nsIUpdate object at the specified index


## updateCount ##

Gets the total number of updates in the history list.


## activeUpdate ##

The active (current) update. The active update is not in the history list.


## saveUpdates ##

Saves all updates to disk.


## refreshUpdateStatus ##

Refresh the update status based on the information in update.status.

