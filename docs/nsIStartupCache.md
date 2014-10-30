---
layout: default
---

# nsIStartupCache #

## Methods ##

### getBuffer ###
 This interface is provided for testing purposes only, basically  
 just to solve link vagaries. See docs in StartupCache.h  
 GetBuffer, PutBuffer, and InvalidateCache act as described   
 in that file. */  

### putBuffer ###

### invalidateCache ###

### ignoreDiskCache ###

### getDebugObjectOutputStream ###
 In debug builds, wraps this object output stream with a stream that will   
 detect and prevent the write of a multiply-referenced non-singleton object   
 during serialization. In non-debug, returns an add-ref'd pointer to  
 original stream, unwrapped. */  

### startupWriteComplete ###

### resetStartupWriteTimer ###

### recordAgesAlways ###

## Attributes ##

### observer ###
