---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIThreadRetargetableRequest.idl">Source file</a>
</div>

# nsIThreadRetargetableRequest #
<code>  
nsIThreadRetargetableRequest  
  
Should be implemented by requests that support retargeting delivery of  
data off the main thread.  
  
</code>
## Methods ##

### retargetDeliveryTo(aNewTarget) ###
<code>  
Called to retarget delivery of OnDataAvailable to another thread. Should  
only be called before AsyncOpen for nsIWebsocketChannels, or during  
OnStartRequest for nsIChannels.  
Note: For nsIChannels, OnStartRequest and OnStopRequest will still be  
delivered on the main thread.  
  
@param aNewTarget New event target, e.g. thread or threadpool.  
  
Note: no return value is given. If the retargeting cannot be handled,  
normal delivery to the main thread will continue. As such, listeners  
should be ready to deal with OnDataAvailable on either the main thread or  
the new target thread.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aNewTarget</td>
<td>New event target, e.g. thread or threadpool.  
</td>
</tr>

</table>
