---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIForcePendingChannel.idl">Source file</a>
</div>

# nsIForcePendingChannel #
  
nsIForcePending interface exposes a function that enables overwriting of the normal   
behavior for the channel's IsPending(), forcing 'true' to be returned.  
  

## Methods ##

### forcePending(aForcePending) ###
  
forcePending(true) overrides the normal behavior for the   
channel's IsPending(), forcing 'true' to be returned. A call to  
forcePending(false) reverts IsPending() back to normal behavior.  
  
