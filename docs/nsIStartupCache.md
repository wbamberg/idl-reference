---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/startupcache/nsIStartupCache.idl">Source file</a>
</div>

# nsIStartupCache #

## Methods ##

### getBuffer(aID, aBuffer) ###
<code> This interface is provided for testing purposes only, basically  
 just to solve link vagaries. See docs in StartupCache.h  
 GetBuffer, PutBuffer, and InvalidateCache act as described   
 in that file. */  
</code>
### putBuffer(aID, aBuffer, aLength) ###

### invalidateCache() ###

### ignoreDiskCache() ###

### getDebugObjectOutputStream(aStream) ###
<code> In debug builds, wraps this object output stream with a stream that will   
 detect and prevent the write of a multiply-referenced non-singleton object   
 during serialization. In non-debug, returns an add-ref'd pointer to  
 original stream, unwrapped. */  
</code>
### startupWriteComplete() ###

### resetStartupWriteTimer() ###

### recordAgesAlways() ###

## Attributes ##

### observer ###
