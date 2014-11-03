---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/network/interfaces/nsITCPSocketChild.idl">Source file</a>
</div>

# nsITCPSocketChild #

## Methods ##

### sendOpen(socket, host, port, ssl, binaryType, window, windowVal) ###

### sendSend(data, byteOffset, byteLength, trackingNumber) ###

### sendResume() ###

### sendSuspend() ###

### sendClose() ###

### sendStartTLS() ###

### setSocketAndWindow(socket, windowVal) ###
<code>  
Initialize the TCP socket on the child side for IPC. It is called from the child side,  
which is generated in receiving a notification of accepting any open request  
on the parent side. We use single implementation that works on a child process   
as well as in the single process model.  
  
@param socket  
       The TCP socket on the child side.  
       This instance is connected with the child IPC side of the IPC bridge.  
@param windowVal  
       The window object on the child side to create data  
       as "jsval" for deserialization.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>socket</td>
<td>       The TCP socket on the child side.  
       This instance is connected with the child IPC side of the IPC bridge.  
</td>
</tr>

<tr>
<td>windowVal</td>
<td>       The window object on the child side to create data  
       as "jsval" for deserialization.  
</td>
</tr>

</table>

## Attributes ##

### host ###

### port ###
