---
layout: default
---

# nsIStreamListenerTee #
  
As data "flows" into a stream listener tee, it is copied to the output stream  
and then forwarded to the real listener.  
  

## Methods ##

### init(listener, sink, requestObserver) ###
   
Initalize the tee.  
  
@param listener  
   the original listener the tee will propagate onStartRequest,  
   onDataAvailable and onStopRequest notifications to, exceptions from   
   the listener will be propagated back to the channel  
@param sink  
   the stream the data coming from the channel will be written to,  
   should be blocking  
@param requestObserver  
   optional parameter, listener that gets only onStartRequest and  
   onStopRequest notifications; exceptions threw within this optional  
   observer are also propagated to the channel, but exceptions from  
   the original listener (listener parameter) are privileged   
  

#### Parameters ####

<table>

<tr>
<td>listener</td>
<td>   the original listener the tee will propagate onStartRequest,  
   onDataAvailable and onStopRequest notifications to, exceptions from   
   the listener will be propagated back to the channel  
</td>
</tr>

<tr>
<td>sink</td>
<td>   the stream the data coming from the channel will be written to,  
   should be blocking  
</td>
</tr>

<tr>
<td>requestObserver</td>
<td>   optional parameter, listener that gets only onStartRequest and  
   onStopRequest notifications; exceptions threw within this optional  
   observer are also propagated to the channel, but exceptions from  
   the original listener (listener parameter) are privileged   
</td>
</tr>

</table>

### initAsync(listener, eventTarget, sink, requestObserver) ###
   
Initalize the tee like above, but with the extra parameter to make it  
possible to copy the output asynchronously  
@param anEventTarget  
   if set, this event-target is used to copy data to the output stream,  
   giving an asynchronous tee  
  

#### Parameters ####

<table>

<tr>
<td>anEventTarget</td>
<td>   if set, this event-target is used to copy data to the output stream,  
   giving an asynchronous tee  
</td>
</tr>

</table>
