---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/network/interfaces/nsIDOMTCPSocket.idl">Source file</a>
</div>

# nsITCPSocketEvent #
  
nsITCPSocketEvent is the event object which is passed as the  
first argument to all the event handler callbacks. It contains  
the socket that was associated with the event, the type of event,  
and the data associated with the event (if any).  
  

## Attributes ##

### target ###
  
The socket object which produced this event.  
  

### type ###
  
The type of this event. One of:  
  
open  
error  
data  
drain  
close  
  

### data ###
  
The data related to this event, if any. In the ondata callback,  
data will be the bytes read from the network; if the binaryType  
of the socket was "arraybuffer", this value will be of type ArrayBuffer;  
otherwise, it will be a normal JavaScript string.  
  
In the onerror callback, data will be a string with a description  
of the error.  
  
In the other callbacks, data will be an empty string.  
  
