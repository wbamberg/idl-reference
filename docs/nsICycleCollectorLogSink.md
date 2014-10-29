---
layout: default
---

# nsICycleCollectorLogSink #

This interface allows replacing the log-writing backend for an
nsICycleCollectorListener.  As this interface is also called while
the cycle collector is running, it cannot be implemented in JS.


## Methods ##

### open ###

### closeGCLog ###

### closeCCLog ###

## Attributes ##

### filenameIdentifier ###

### processIdentifier ###

### gcLog ###

### ccLog ###
