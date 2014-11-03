---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/events/nsIEventListenerService.idl">Source file</a>
</div>

# nsIEventListenerService #

## Methods ##

### getListenerInfoFor(aEventTarget, aCount, aOutArray) ###
<pre>  
Returns an array of nsIEventListenerInfo objects.  
If aEventTarget doesn't have any listeners, this returns null.  
  
</pre>
### getEventTargetChainFor(aEventTarget, aCount, aOutArray) ###
<pre>  
Returns an array of event targets.  
aEventTarget will be at index 0.  
The objects are the ones that would be used as DOMEvent.currentTarget while  
dispatching an event to aEventTarget  
@note Some events, especially 'load', may actually have a shorter  
      event target chain than what this methods returns.  
  
</pre>
### hasListenersFor(aEventTarget, aType) ###
<pre>  
Returns true if a event target has any listener for the given type.  
  
</pre>
### addSystemEventListener(target, type, listener, useCapture) ###
<pre>  
Add a system-group eventlistener to a event target.  
  
</pre>
### removeSystemEventListener(target, type, listener, useCapture) ###
<pre>  
Remove a system-group eventlistener from a event target.  
  
</pre>
### addListenerForAllEvents(target, listener, aUseCapture, aWantsUntrusted, aSystemEventGroup) ###

### removeListenerForAllEvents(target, listener, aUseCapture, aSystemEventGroup) ###
