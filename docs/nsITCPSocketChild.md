---
layout: default
---

# nsITCPSocketChild #

## Methods ##

### sendOpen ###

### sendSend ###

### sendResume ###

### sendSuspend ###

### sendClose ###

### sendStartTLS ###

### setSocketAndWindow ###

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


## Attributes ##

### host ###

### port ###
