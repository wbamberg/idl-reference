---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsIHttpEventSink.idl">Source file</a>
</div>

# nsIHttpEventSink #
  
nsIHttpEventSink  
  
Implement this interface to receive control over various HTTP events.  The  
HTTP channel will try to get this interface from its notificationCallbacks  
attribute, and if it doesn't find it there it will look for it from its  
loadGroup's notificationCallbacks attribute.  
  
These methods are called before onStartRequest, and should be handled  
SYNCHRONOUSLY.  
  
@deprecated Newly written code should use nsIChannelEventSink instead of this  
interface.  
  

## Methods ##

### onRedirect(httpChannel, newChannel) ###
  
Called when a redirect occurs due to a HTTP response like 302.  The  
redirection may be to a non-http channel.  
  
  

#### Returns ####

<table>

<tr>
<td>failure cancels redirect  
</td>
</tr>

</table>
