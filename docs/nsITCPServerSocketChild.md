---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/network/interfaces/nsITCPServerSocketChild.idl">Source file</a>
</div>

# nsITCPServerSocketChild #
<pre>  
Interface to allow the content process server socket to reach the IPC bridge.  
It is used in the server socket implementation on the child side.  
  
</pre>
## Methods ##

### listen(serverSocket, port, backlog, binaryType) ###
<pre>  
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
  
</pre>
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
<pre>  
Tell the chrome process to close the server socket.  
  
</pre>