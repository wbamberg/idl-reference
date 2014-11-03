---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/events/nsIEventListenerService.idl">Source file</a>
</div>

# nsIEventListenerInfo #
<pre>  
An instance of this interface describes how an event listener  
was added to an event target.  
  
</pre>
## Methods ##

### toSource() ###
<pre>  
Tries to serialize event listener to a string.  
Returns null if serialization isn't possible  
(for example with C++ listeners).  
  
</pre>
## Attributes ##

### type ###
<pre>  
The type of the event for which the listener was added.  
Null if the listener is for all the events.  
  
</pre>
### capturing ###

### allowsUntrusted ###

### inSystemEventGroup ###

### listenerObject ###
<pre>  
The underlying JS object of the event listener, if this listener  
has one.  Null otherwise.  
  
</pre>