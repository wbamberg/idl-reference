---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/network/interfaces/nsITCPServerSocketChild.idl">Source file</a>
</div>

# nsITCPServerSocketChild #
  
Interface to allow the content process server socket to reach the IPC bridge.  
It is used in the server socket implementation on the child side.  
  

## Methods ##

### listen(serverSocket, port, backlog, binaryType) ###
  
Tell the chrome process to listen on the port with the given parameters.  
  
  

#### Parameters ####

<table>

<tr>
<td>serverSocket</td>
<td>       The server socket generated in the listen of nsIDOMTCPSocket  
       on the child side.  
</td>
</tr>

<tr>
<td>port</td>
<td>       The port of the server socket.  
</td>
</tr>

<tr>
<td>backlog</td>
<td>       The maximum length the queue of pending connections may grow to.  
</td>
</tr>

<tr>
<td>binaryType</td>
<td>       "arraybuffer" to use UInt8 array instances or "string" to use String.  
</td>
</tr>

</table>

### close() ###
  
Tell the chrome process to close the server socket.  
  
