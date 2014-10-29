---
layout: default
---

# nsITCPServerSocketInternal #

Internal interfaces for use in cross-process server-socket implementation.
Needed to account for multiple possible types that can be provided to
the socket callbacks as arguments.

These interfaces are for calling each method from the server socket object
on the parent and child side for an IPC protocol implementation.


## init ##

Initialization after creating a TCP server socket object.

@param windowVal
       An object to create ArrayBuffer for this window. See Bug 831107.


## listen ##
 
Listen on a port

@param localPort 
       The port of the server socket. Pass -1 to indicate no preference,
       and a port will be selected automatically.
@param options 
       An object specifying one or more parameters which
       determine the details of the socket.

       binaryType: "arraybuffer" to use UInt8 array
       instances in the ondata callback and as the argument
       to send. Defaults to "string", to use JavaScript strings.
@param backlog 
       The maximum length the queue of pending connections may grow to.
       This parameter may be silently limited by the operating system.
       Pass -1 to use the default value.


## callListenerAccept ##

Listener for receiving an accepted socket.


## callListenerError ##

Listener for handling an error caused in chrome process.

