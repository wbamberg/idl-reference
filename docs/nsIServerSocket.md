---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIServerSocket.idl">Source file</a>
</div>

# nsIServerSocket #
  
nsIServerSocket  
  
An interface to a server socket that can accept incoming connections.  
  

## Methods ##

### init(aPort, aLoopbackOnly, aBackLog) ###
 @} */  
  
init  
  
This method initializes a server socket.  
  
@param aPort  
       The port of the server socket.  Pass -1 to indicate no preference,  
       and a port will be selected automatically.  
@param aLoopbackOnly  
       If true, the server socket will only respond to connections on the  
       local loopback interface.  Otherwise, it will accept connections  
       from any interface.  To specify a particular network interface,  
       use initWithAddress.  
@param aBackLog  
       The maximum length the queue of pending connections may grow to.  
       This parameter may be silently limited by the operating system.  
       Pass -1 to use the default value.  
  

#### Parameters ####

<table>

<tr>
<td>aPort</td>
<td>       The port of the server socket.  Pass -1 to indicate no preference,  
       and a port will be selected automatically.  
</td>
</tr>

<tr>
<td>aLoopbackOnly</td>
<td>       If true, the server socket will only respond to connections on the  
       local loopback interface.  Otherwise, it will accept connections  
       from any interface.  To specify a particular network interface,  
       use initWithAddress.  
</td>
</tr>

<tr>
<td>aBackLog</td>
<td>       The maximum length the queue of pending connections may grow to.  
       This parameter may be silently limited by the operating system.  
       Pass -1 to use the default value.  
</td>
</tr>

</table>

### initSpecialConnection(aPort, aFlags, aBackLog) ###
  
initSpecialConnection  
  
This method initializes a server socket and offers the ability to have  
that socket not get terminated if Gecko is set offline.  
  
@param aPort  
       The port of the server socket.  Pass -1 to indicate no preference,  
       and a port will be selected automatically.  
@param aFlags  
       Flags for the socket.  
@param aBackLog  
       The maximum length the queue of pending connections may grow to.  
       This parameter may be silently limited by the operating system.  
       Pass -1 to use the default value.  
  

#### Parameters ####

<table>

<tr>
<td>aPort</td>
<td>       The port of the server socket.  Pass -1 to indicate no preference,  
       and a port will be selected automatically.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>       Flags for the socket.  
</td>
</tr>

<tr>
<td>aBackLog</td>
<td>       The maximum length the queue of pending connections may grow to.  
       This parameter may be silently limited by the operating system.  
       Pass -1 to use the default value.  
</td>
</tr>

</table>

### initWithAddress(aAddr, aBackLog) ###
  
initWithAddress  
  
This method initializes a server socket, and binds it to a particular  
local address (and hence a particular local network interface).  
  
@param aAddr  
       The address to which this server socket should be bound.  
@param aBackLog  
       The maximum length the queue of pending connections may grow to.  
       This parameter may be silently limited by the operating system.  
       Pass -1 to use the default value.  
  

#### Parameters ####

<table>

<tr>
<td>aAddr</td>
<td>       The address to which this server socket should be bound.  
</td>
</tr>

<tr>
<td>aBackLog</td>
<td>       The maximum length the queue of pending connections may grow to.  
       This parameter may be silently limited by the operating system.  
       Pass -1 to use the default value.  
</td>
</tr>

</table>

### initWithFilename(aPath, aPermissions, aBacklog) ###
  
initWithFilename  
  
This method initializes a Unix domain or "local" server socket. Such  
a socket has a name in the filesystem, like an ordinary file. To  
connect, a client supplies the socket's filename, and the usual  
permission checks on socket apply.  
  
This makes Unix domain sockets useful for communication between the  
programs being run by a specific user on a single machine: the  
operating system takes care of authentication, and the user's home  
directory or profile directory provide natural per-user rendezvous  
points.  
  
Since Unix domain sockets are always local to the machine, they are  
not affected by the nsIIOService's 'offline' flag.  
  
The system-level socket API may impose restrictions on the length of  
the filename that are stricter than those of the underlying  
filesystem. If the file name is too long, this returns  
NS_ERROR_FILE_NAME_TOO_LONG.  
  
All components of the path prefix of |aPath| must name directories;  
otherwise, this returns NS_ERROR_FILE_NOT_DIRECTORY.  
  
This call requires execute permission on all directories containing  
the one in which the socket is to be created, and write and execute  
permission on the directory itself. Otherwise, this returns  
NS_ERROR_CONNECTION_REFUSED.  
  
This call creates the socket's directory entry. There must not be  
any existing entry with the given name. If there is, this returns  
NS_ERROR_SOCKET_ADDRESS_IN_USE.  
  
On systems that don't support Unix domain sockets at all, this  
returns NS_ERROR_SOCKET_ADDRESS_NOT_SUPPORTED.  
  
@param aPath nsIFile  
       The file name at which the socket should be created.  
  
@param aPermissions unsigned long  
       Unix-style permission bits to be applied to the new socket.  
  
Note about permissions: Linux's unix(7) man page claims that some  
BSD-derived systems ignore permissions on UNIX-domain sockets;  
NetBSD's bind(2) man page agrees, but says it does check now (dated  
2005). POSIX has required 'connect' to fail if write permission on  
the socket itself is not granted since 2003 (Issue 6). NetBSD says  
that the permissions on the containing directory (execute) have  
always applied, so creating sockets in appropriately protected  
directories should be secure on both old and new systems.  
  

#### Parameters ####

<table>

<tr>
<td>aPath</td>
<td>nsIFile  
       The file name at which the socket should be created.  
</td>
</tr>

<tr>
<td>aPermissions</td>
<td>unsigned long  
       Unix-style permission bits to be applied to the new socket.  
</td>
</tr>

</table>

### close() ###
  
close  
  
This method closes a server socket.  This does not affect already  
connected client sockets (i.e., the nsISocketTransport instances  
created from this server socket).  This will cause the onStopListening  
event to asynchronously fire with a status of NS_BINDING_ABORTED.  
  

### asyncListen(aListener) ###
  
asyncListen  
  
This method puts the server socket in the listening state.  It will  
asynchronously listen for and accept client connections.  The listener  
will be notified once for each client connection that is accepted.  The  
listener's onSocketAccepted method will be called on the same thread  
that called asyncListen (the calling thread must have a nsIEventTarget).  
  
The listener will be passed a reference to an already connected socket  
transport (nsISocketTransport).  See below for more details.  
  
@param aListener  
       The listener to be notified when client connections are accepted.  
  

#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>       The listener to be notified when client connections are accepted.  
</td>
</tr>

</table>

### getAddress() ###
  
Returns the address to which this server socket is bound.  Since a  
server socket may be bound to multiple network devices, this address  
may not necessarily be specific to a single network device.  In the  
case of an IP socket, the IP address field would be zerod out to  
indicate a server socket bound to all network devices.  Therefore,  
this method cannot be used to determine the IP address of the local  
system.  See nsIDNSService::myHostName if this is what you need.  
  

## Attributes ##

### port ###
  
Returns the port of this server socket.  
  

## Constants ##

### LoopbackOnly ###
  
@name Server Socket Flags  
These flags define various socket options.  
@{  
  

### KeepWhenOffline ###
