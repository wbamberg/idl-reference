---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIServiceWorkerManager.idl">Source file</a>
</div>

# nsIServiceWorkerManager #

## Methods ##

### register(aScope, aScriptURI) ###
<code>  
Registers a ServiceWorker with script loaded from `aScriptURI` to act as  
the ServiceWorker for aScope.  Requires a valid entry settings object on  
the stack. This means you must call this from content code 'within'  
a window.  
  
Returns a Promise.  
  
</code>
### unregister(aCallback, aScope) ###
<code>  
Unregister an existing ServiceWorker registration for `aScope`.  
It keeps aCallback alive until the operation is concluded.  
  
</code>
### getRegistrations(aWindow) ###

### getRegistration(aWindow, aScope) ###

### getReadyPromise(aWindow) ###

### removeReadyPromise(aWindow) ###

### AddRegistrationEventListener(aPageURI, aTarget) ###

### RemoveRegistrationEventListener(aPageURI, aTarget) ###

### MaybeStartControlling(aDoc) ###
<code>  
Call this to request that document `aDoc` be controlled by a ServiceWorker  
if a registration exists for it's scope.  
  
This MUST only be called once per document!  
  
</code>
### MaybeStopControlling(aDoc) ###
<code>  
Documents that have called MaybeStartControlling() should call this when  
they are destroyed. This function may be called multiple times, and is  
idempotent.  
  
</code>
### GetInstalling(aWindow, aScope) ###

### GetWaiting(aWindow, aScope) ###

### GetActive(aWindow, aScope) ###

### GetDocumentController(aWindow) ###

### getScopeForUrl(path) ###
