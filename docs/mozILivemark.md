---
layout: default
---

# mozILivemark #

## Methods ##

### reload ###

Reload livemark contents if they are expired or if forced to do so.

@param [optional]aForceUpdate
       If set to true forces a reload even if contents are still valid.

@note The update process is asynchronous, it's possible to register a
      result observer to be notified of updated contents through
      registerForUpdates.


### getNodesForContainer ###

Returns an array of nsINavHistoryResultNode objects, representing children
of this livemark.  The nodes will have aContainerNode as parent.

@param aContainerNode
       Object implementing nsINavHistoryContainerResultNode, to be used as
       parent of the livemark nodes.


### registerForUpdates ###

Registers a container node for updates on this livemark.
When the livemark contents change, an invalidateContainer(aContainerNode)
request is sent to aResultObserver.

@param aContainerNode
       Object implementing nsINavHistoryContainerResultNode, representing
       this livemark.
@param aResultObserver
       The nsINavHistoryResultObserver that should be notified of changes
       to the livemark contents.


### unregisterForUpdates ###

Unregisters a previously registered container node.

@param aContainerNode
       Object implementing nsINavHistoryContainerResultNode, representing
       this livemark.

@note it's suggested to always unregister containers that are no more used,
      to free up the associated resources.  A good time to do so is when
      the container gets closed.


## Attributes ##

### status ###

Status of this livemark.  One of the STATUS_* constants above.


## Constants ##

### STATUS_READY ###

### STATUS_LOADING ###

### STATUS_FAILED ###
