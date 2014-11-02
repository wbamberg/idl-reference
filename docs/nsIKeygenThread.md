---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIKeygenThread.idl">Source file</a>
</div>

# nsIKeygenThread #
  
nsIKeygenThread  
 This is used to communicate with the thread generating a key pair,  
 to be used by the dialog displaying status information.  
  

## Methods ##

### startKeyGeneration(observer) ###
  
startKeyGeneration - run the thread  
  A user interface using this interface needs to  
  call this method as soon as the status information  
  is displaying. This will trigger key generation.  
  To allow the closure of the status information,  
  the thread needs a handle to an observer.  
  
  observer will be called on the UI thread.  
  When the key generation is done, the observe method will  
  be called with a topic of "keygen-finished" and null data  
  and subject.  
  

### userCanceled(threadAlreadyClosedDialog) ###
  
userCanceled - notify the thread  
  If the user canceled, the thread is no longer allowed to  
  close the dialog. However, if the thread already closed  
  it, we are not allowed to close it.  
  
