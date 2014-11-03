---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIThreadRetargetableStreamListener.idl">Source file</a>
</div>

# nsIThreadRetargetableStreamListener #
  
nsIThreadRetargetableStreamListener  
  
To be used by classes which implement nsIStreamListener and whose  
OnDataAvailable callback may be retargeted for delivery off the main thread.  
  

## Methods ##

### checkListenerChain() ###
  
Checks this listener and any next listeners it may have to verify that  
they can receive OnDataAvailable off the main thread. It is the  
responsibility of the implementing class to decide on the criteria to  
determine if retargeted delivery of these methods is possible, but it must  
check any and all nsIStreamListener objects that might be called in the  
listener chain.  
  
An exception should be thrown if a listener in the chain does not  
support retargeted delivery, i.e. if the next listener does not implement  
nsIThreadRetargetableStreamListener, or a call to its checkListenerChain()  
fails.  
  
