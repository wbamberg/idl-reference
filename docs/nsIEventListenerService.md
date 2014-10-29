---
layout: default
---

# nsIEventListenerService #

## Methods ##

### getListenerInfoFor ###

Returns an array of nsIEventListenerInfo objects.
If aEventTarget doesn't have any listeners, this returns null.


### getEventTargetChainFor ###

Returns an array of event targets.
aEventTarget will be at index 0.
The objects are the ones that would be used as DOMEvent.currentTarget while
dispatching an event to aEventTarget
@note Some events, especially 'load', may actually have a shorter
      event target chain than what this methods returns.


### hasListenersFor ###

Returns true if a event target has any listener for the given type.


### addSystemEventListener ###

Add a system-group eventlistener to a event target.


### removeSystemEventListener ###

Remove a system-group eventlistener from a event target.


### addListenerForAllEvents ###

### removeListenerForAllEvents ###
