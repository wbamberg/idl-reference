---
layout: default
---

# nsIServerSocketListener #
  
nsIServerSocketListener  
  
This interface is notified whenever a server socket accepts a new connection.  
The transport is in the connected state, and read/write streams can be opened  
using the normal nsITransport API.  The address of the client can be found by  
calling the nsISocketTransport::GetAddress method or by inspecting  
nsISocketTransport::GetHost, which returns a string representation of the  
client's IP address (NOTE: this may be an IPv4 or IPv6 string literal).  
  

## Methods ##

### onSocketAccepted(aServ, aTransport) ###
  
onSocketAccepted  
  
This method is called when a client connection is accepted.  
  
@param aServ  
       The server socket.  
@param aTransport  
       The connected socket transport.  
  

#### Parameters ####

<table>

<tr>
<td>aServ</td>
<td>       The server socket.  
</td>
</tr>

<tr>
<td>aServ</td>
<td>       The server socket.  
</td>
</tr>

</table>

### onStopListening(aServ, aStatus) ###
  
onStopListening  
  
This method is called when the listening socket stops for some reason.  
The server socket is effectively dead after this notification.  
  
@param aServ  
       The server socket.  
@param aStatus  
       The reason why the server socket stopped listening.  If the  
       server socket was manually closed, then this value will be  
       NS_BINDING_ABORTED.  
  

#### Parameters ####

<table>

<tr>
<td>aServ</td>
<td>       The server socket.  
</td>
</tr>

<tr>
<td>aServ</td>
<td>       The server socket.  
</td>
</tr>

</table>
