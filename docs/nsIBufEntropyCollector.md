---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/boot/public/nsIBufEntropyCollector.idl">Source file</a>
</div>
# nsIBufEntropyCollector #

## Methods ##

### forwardTo(collector) ###
  
Forward the entropy collected so far to |collector| and then  
continue forwarding new entropy as it arrives.  
  

### dontForward() ###
  
No longer forward to a (possibly) previously remembered collector.  
Do buffering again.  
  
