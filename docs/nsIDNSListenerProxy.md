---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/dns/nsIDNSListener.idl">Source file</a>
</div>
# nsIDNSListenerProxy #
  
nsIDNSListenerProxy:  
  
Must be implemented by classes that wrap the original listener passed to  
nsIDNSService.AsyncResolve, so we have access to original listener for  
comparison purposes.  
  

## Attributes ##

### originalListener ###
