---
layout: default
---

# nsIServiceWorkerManager #

## Methods ##

### register ###

Registers a ServiceWorker with script loaded from `aScriptURI` to act as
the ServiceWorker for aScope.  Requires a valid entry settings object on
the stack. This means you must call this from content code 'within'
a window.

Returns a Promise.


### unregister ###

Unregister an existing ServiceWorker registration for `aScope`.
It keeps aCallback alive until the operation is concluded.


### getRegistrations ###

### getRegistration ###

### getReadyPromise ###

### removeReadyPromise ###

### AddRegistrationEventListener ###

### RemoveRegistrationEventListener ###

### MaybeStartControlling ###

Call this to request that document `aDoc` be controlled by a ServiceWorker
if a registration exists for it's scope.

This MUST only be called once per document!


### MaybeStopControlling ###

Documents that have called MaybeStartControlling() should call this when
they are destroyed. This function may be called multiple times, and is
idempotent.


### GetInstalling ###

### GetWaiting ###

### GetActive ###

### GetDocumentController ###

### getScopeForUrl ###
