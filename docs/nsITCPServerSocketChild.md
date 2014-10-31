---
layout: default
---

# nsITCPServerSocketChild #
  
Interface to allow the content process server socket to reach the IPC bridge.  
It is used in the server socket implementation on the child side.  
  

## Methods ##

### listen(serverSocket, port, backlog, binaryType) ###
  
Tell the chrome process to listen on the port with the given parameters.  
  
@param serverSocket  
       The server socket generated in the listen of nsIDOMTCPSocket  
       on the child side.  
@param port  
       The port of the server socket.  
@param backlog   
       The maximum length the queue of pending connections may grow to.  
@param binaryType  
       "arraybuffer" to use UInt8 array instances or "string" to use String.  
  

#### Parameters ####

<table>

<tr>
<td>serverSocket</td>
<td>       The server socket generated in the listen of nsIDOMTCPSocket  
       on the child side.  
</td>
</tr>

<tr>
<td>serverSocket</td>
<td>       The server socket generated in the listen of nsIDOMTCPSocket  
       on the child side.  
</td>
</tr>

<tr>
<td>serverSocket</td>
<td>       The server socket generated in the listen of nsIDOMTCPSocket  
       on the child side.  
</td>
</tr>

<tr>
<td>serverSocket</td>
<td>       The server socket generated in the listen of nsIDOMTCPSocket  
       on the child side.  
</td>
</tr>

</table>

### close() ###
  
Tell the chrome process to close the server socket.  
  
