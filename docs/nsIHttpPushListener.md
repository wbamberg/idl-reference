---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIHttpPushListener.idl">Source file</a>
</div>

# nsIHttpPushListener #
  
nsIHttpPushListener  
  
Used for triggering when a HTTP/2 push is received.  
  
  

## Methods ##

### onPush(associatedChannel, pushChannel) ###
  
When provided as a notificationCallback to an httpChannel, this.onPush()  
will be invoked when there is a >= Http2 push to that  
channel. The push may be in progress.  
  
The consumer must start the new channel in the usual way by calling  
pushChannel.AsyncOpen with a nsIStreamListener object that  
will receive the normal sequence of OnStartRequest(),  
0 to N OnDataAvailable(), and onStopRequest().  
  
The new channel can be canceled after the AsyncOpen if it is not wanted.  
  
@param associatedChannel  
       the monitor channel that was recieved on  
@param pushChannel  
       a channel to the resource which is being pushed  
  

#### Parameters ####

<table>

<tr>
<td>associatedChannel</td>
<td>       the monitor channel that was recieved on  
</td>
</tr>

<tr>
<td>pushChannel</td>
<td>       a channel to the resource which is being pushed  
</td>
</tr>

</table>
