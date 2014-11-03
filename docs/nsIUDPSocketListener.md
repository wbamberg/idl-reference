---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIUDPSocket.idl">Source file</a>
</div>

# nsIUDPSocketListener #
<pre>  
nsIUDPSocketListener  
  
This interface is notified whenever a UDP socket accepts a new connection.  
The transport is in the connected state, and read/write streams can be opened  
using the normal nsITransport API.  The address of the client can be found by  
calling the nsISocketTransport::GetAddress method or by inspecting  
nsISocketTransport::GetHost, which returns a string representation of the  
client's IP address (NOTE: this may be an IPv4 or IPv6 string literal).  
  
</pre>
## Methods ##

### onPacketReceived(aSocket, aMessage) ###
<pre>  
onPacketReceived  
  
This method is called when a client sends an UDP packet.  
  
@param aSocket  
       The UDP socket.  
@param aMessage  
       The message.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aSocket</td>
<td>       The UDP socket.  
</td>
</tr>

<tr>
<td>aMessage</td>
<td>       The message.  
</td>
</tr>

</table>

### onStopListening(aSocket, aStatus) ###
<pre>  
onStopListening  
  
This method is called when the listening socket stops for some reason.  
The UDP socket is effectively dead after this notification.  
  
@param aSocket  
       The UDP socket.  
@param aStatus  
       The reason why the UDP socket stopped listening.  If the  
       UDP socket was manually closed, then this value will be  
       NS_BINDING_ABORTED.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aSocket</td>
<td>       The UDP socket.  
</td>
</tr>

<tr>
<td>aStatus</td>
<td>       The reason why the UDP socket stopped listening.  If the  
       UDP socket was manually closed, then this value will be  
       NS_BINDING_ABORTED.  
</td>
</tr>

</table>
