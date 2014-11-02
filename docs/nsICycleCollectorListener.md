---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsICycleCollectorListener.idl">Source file</a>
</div>
# nsICycleCollectorListener #
  
Given an instance of this interface, the cycle collector calls the instance's  
methods to report the objects it visits, the edges between them, and its  
conclusions about which objects are roots and which are garbage.  
  
For a single cycle collection pass, the cycle collector calls this  
interface's methods in the following order:  
  
- First, |begin|. If |begin| returns an error, none of the listener's other  
  methods will be called.  
  
- Then, for each node in the graph:  
  - a call to either |noteRefCountedObject| or |noteGCedObject|, to describe  
    the node itself; and  
  - for each edge starting at that node, a call to |noteEdge|.  
  
- Then, zero or more calls to |noteIncrementalRoot|; an "incremental  
  root" is an object that may have had a new reference to it created  
  during an incremental collection, and must therefore be treated as  
  live for safety.  
  
- After all the nodes have been described, a call to |beginResults|.  
  
- A series of calls to:  
  - |describeRoot|, for reference-counted nodes that the CC has identified as  
    roots of collection. (The cycle collector didn't find enough incoming  
    edges to account for these nodes' reference counts, so there must be code  
    holding on to them that the cycle collector doesn't know about.)  
  - |describeGarbage|, for nodes the cycle collector has identified as garbage.  
  
  Any node not mentioned in a call to |describeRoot| or |describeGarbage| is  
  neither a root nor garbage. (The cycle collector was able to find all the  
  edges implied by the node's reference count.)  
  
- Finally, a call to |end|.  
  
  
This interface cannot be implemented by JavaScript code, as it is called  
while the cycle collector is running. To analyze cycle collection data in JS:  
  
- Create an instance of @mozilla.org/cycle-collector-logger;1, which  
  implements this interface.  
  
- Set its |disableLog| property to true. This prevents the logger from  
  printing messages about each method call to a temporary log file.  
  
- Set its |wantAfterProcessing| property to true. This tells the logger  
  to record calls to its methods in memory. The |processNext| method  
  returns events from this record.  
  
- Perform a collection using the logger. For example, call  
  |nsIDOMWindowUtils|'s |garbageCollect| method, passing the logger as  
  the |aListener| argument.  
  
- When the collection is complete, loop calling the logger's  
  |processNext| method, passing a JavaScript object that implements  
  nsICycleCollectorHandler. This JS code is free to allocate and operate  
  on objects however it pleases: the cycle collector has finished its  
  work, and the JS code is simply consuming recorded data.  
  

## Methods ##

### allTraces() ###

### begin() ###

### noteRefCountedObject(aAddress, aRefCount, aObjectDescription) ###

### noteGCedObject(aAddress, aMarked, aObjectDescription, aCompartmentAddress) ###

### noteEdge(aToAddress, aEdgeName) ###

### noteWeakMapEntry(aMap, aKey, aKeyDelegate, aValue) ###

### noteIncrementalRoot(aAddress) ###

### beginResults() ###

### describeRoot(aAddress, aKnownEdges) ###

### describeGarbage(aAddress) ###

### end() ###

### processNext(aHandler) ###

## Attributes ##

### wantAllTraces ###

### disableLog ###

### logSink ###

### wantAfterProcessing ###
