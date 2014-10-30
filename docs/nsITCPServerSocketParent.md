---
layout: default
---

# nsITCPServerSocketParent #
   
Interface required to allow the TCP server-socket object in the parent process  
to talk to the parent IPC actor.  
It is used in the server socket implementation on the parent side.  
  

## Methods ##

### sendCallbackAccept(socket) ###
  
Trigger a callback in the content process when the socket accepts any request.  
  
@param socket  
       The socket generated in accepting any open request on the parent side.  
  

### sendCallbackError(message, filename, lineNumber, columnNumber) ###
  
Trigger a callback in the content process when an error occurs.  
  
@param message  
       The error message.  
@param filename  
       The file name in which the error occured.  
@param lineNumber  
       The line number in which the error occured.  
@param columnNumber  
       The column number in which the error occured.  
  
