---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsICycleCollectorListener.idl">Source file</a>
</div>

# nsICycleCollectorLogSink #
  
This interface allows replacing the log-writing backend for an  
nsICycleCollectorListener.  As this interface is also called while  
the cycle collector is running, it cannot be implemented in JS.  
  

## Methods ##

### open(aGCLog, aCCLog) ###

### closeGCLog() ###

### closeCCLog() ###

## Attributes ##

### filenameIdentifier ###

### processIdentifier ###

### gcLog ###

### ccLog ###
