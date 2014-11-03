---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsICycleCollectorListener.idl">Source file</a>
</div>

# nsICycleCollectorHandler #
<code>  
Interfaces for observing the cycle collector's work, both from C++ and  
from JavaScript.  
  
If given an object implementing nsICycleCollectorListener, the cycle  
collector calls that object's methods as it works, describing the  
objects it visits, the edges it finds, and the conclusions it reaches  
about which objects are live.  
  
Analyzing cycle collection from JS is harder: an nsICycleCollectorListener  
mustn't mess with the object graph while the cycle collector is trying to  
figure it out, which means it can't be implemented by JS code: JS can't do  
much of anything useful within those constraints. Instead, JS code can  
instantiate @mozilla.org/cycle-collector-logger;1, a C++ class implementing  
nsICycleCollectorListener that logs the cycle collector's mumblings and then  
replays them later to an nsICycleCollectorHandler --- which *can* be  
implemented in JS.  
  
</code><code>  
The interface JS code should implement to receive annotations logged by an  
@mozilla.org/cycle-collector-logger;1 instance. Pass an instance of this to  
the logger's 'processNext' method.  
  
The methods are a subset of those in nsICycleCollectorListener; see the  
descriptions there.  
  
</code>
## Methods ##

### noteRefCountedObject(aAddress, aRefCount, aObjectDescription) ###

### noteGCedObject(aAddress, aMarked, aObjectDescription, aCompartmentAddress) ###

### noteEdge(aFromAddress, aToAddress, aEdgeName) ###

### describeRoot(aAddress, aKnownEdges) ###

### describeGarbage(aAddress) ###
