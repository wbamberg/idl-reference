---
layout: default
---

# nsIBufEntropyCollector #

## Methods ##

### forwardTo(collector) ###
  
Forward the entropy collected so far to |collector| and then  
continue forwarding new entropy as it arrives.  
  

### dontForward() ###
  
No longer forward to a (possibly) previously remembered collector.  
Do buffering again.  
  
