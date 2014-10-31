---
layout: default
---

# nsIChannelEventSink #
  
Implement this interface to receive control over various channel events.  
Channels will try to get this interface from a channel's  
notificationCallbacks or, if not available there, from the loadGroup's  
notificationCallbacks.  
  
These methods are called before onStartRequest.  
  

## Methods ##

### asyncOnChannelRedirect(oldChannel, newChannel, flags, callback) ###
  
Called when a redirect occurs. This may happen due to an HTTP 3xx status  
code. The purpose of this method is to notify the sink that a redirect  
is about to happen, but also to give the sink the right to veto the  
redirect by throwing or passing a failure-code in the callback.  
  
Note that vetoing the redirect simply means that |newChannel| will not  
be opened. It is important to understand that |oldChannel| will continue  
loading as if it received a HTTP 200, which includes notifying observers  
and possibly display or process content attached to the HTTP response.  
If the sink wants to prevent this loading it must explicitly deal with  
it, e.g. by calling |oldChannel->Cancel()|  
  
There is a certain freedom in implementing this method:  
  
If the return-value indicates success, a callback on |callback| is  
required. This callback can be done from within asyncOnChannelRedirect  
(effectively making the call synchronous) or at some point later  
(making the call asynchronous). Repeat: A callback must be done  
if this method returns successfully.  
  
If the return value indicates error (method throws an exception)  
the redirect is vetoed and no callback must be done. Repeat: No  
callback must be done if this method throws!  
  
@see nsIAsyncVerifyRedirectCallback::onRedirectVerifyCallback()  
  
@param oldChannel  
       The channel that's being redirected.  
@param newChannel  
       The new channel. This channel is not opened yet.  
@param flags  
       Flags indicating the type of redirect. A bitmask consisting  
       of flags from above.  
       One of REDIRECT_TEMPORARY and REDIRECT_PERMANENT will always be  
       set.  
@param callback  
       Object to inform about the async result of this method  
  
@throw <any> Throwing an exception will cause the redirect to be  
       cancelled  
  

#### Parameters ####

<table>

<tr>
<td>oldChannel</td>
<td>       The channel that's being redirected.  
</td>
</tr>

<tr>
<td>oldChannel</td>
<td>       The channel that's being redirected.  
</td>
</tr>

<tr>
<td>oldChannel</td>
<td>       The channel that's being redirected.  
</td>
</tr>

<tr>
<td>oldChannel</td>
<td>       The channel that's being redirected.  
</td>
</tr>

</table>

## Constants ##

### REDIRECT_TEMPORARY ###
  
This is a temporary redirect. New requests for this resource should  
continue to use the URI of the old channel.  
  
The new URI may be identical to the old one.  
  

### REDIRECT_PERMANENT ###
  
This is a permanent redirect. New requests for this resource should use  
the URI of the new channel (This might be an HTTP 301 reponse).  
If this flag is not set, this is a temporary redirect.  
  
The new URI may be identical to the old one.  
  

### REDIRECT_INTERNAL ###
  
This is an internal redirect, i.e. it was not initiated by the remote  
server, but is specific to the channel implementation.  
  
The new URI may be identical to the old one.  
  
