---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/network/interfaces/nsIDOMTCPServerSocket.idl">Source file</a>
</div>

# nsIDOMTCPServerSocket #
  
nsIDOMTCPServerSocket  
  
An interface to a server socket that can accept incoming connections for gaia apps.  
  

## Methods ##

### close() ###
  
Close the server socket.  
  

## Attributes ##

### localPort ###
  
The port of this server socket object.  
  

### onconnect ###
  
The onconnect event handler is called when a client connection is accepted.  
The data attribute of the event passed to the onconnect handler will be a TCPSocket  
instance, which is used for communication between client and server.   
  

### onerror ###
  
The onerror handler will be called when the listen of a server socket is aborted.  
The data attribute of the event passed to the onerror handler will have a  
description of the kind of error.  
  
