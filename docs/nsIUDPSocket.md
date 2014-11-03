---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIUDPSocket.idl">Source file</a>
</div>

# nsIUDPSocket #
<pre>  
nsIUDPSocket  
  
An interface to a UDP socket that can accept incoming connections.  
  
</pre>
## Methods ##

### init(aPort, aLoopbackOnly, aAddressReuse) ###
<pre>  
init  
  
This method initializes a UDP socket.  
  
@param aPort  
       The port of the UDP socket.  Pass -1 to indicate no preference,  
       and a port will be selected automatically.  
@param aLoopbackOnly  
       If true, the UDP socket will only respond to connections on the  
       local loopback interface.  Otherwise, it will accept connections  
       from any interface.  To specify a particular network interface,  
       use initWithAddress.  
@param aAddressReuse  
       If true, the socket is allowed to be bound to an address that is  
       already in use. Default is true.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aPort</td>
<td>       The port of the UDP socket.  Pass -1 to indicate no preference,  
       and a port will be selected automatically.  
</td>
</tr>

<tr>
<td>aLoopbackOnly</td>
<td>       If true, the UDP socket will only respond to connections on the  
       local loopback interface.  Otherwise, it will accept connections  
       from any interface.  To specify a particular network interface,  
       use initWithAddress.  
</td>
</tr>

<tr>
<td>aAddressReuse</td>
<td>       If true, the socket is allowed to be bound to an address that is  
       already in use. Default is true.  
</td>
</tr>

</table>

### initWithAddress(aAddr, aAddressReuse) ###
<pre>  
initWithAddress  
  
This method initializes a UDP socket, and binds it to a particular  
local address (and hence a particular local network interface).  
  
@param aAddr  
       The address to which this UDP socket should be bound.  
@param aAddressReuse  
       If true, the socket is allowed to be bound to an address that is  
       already in use. Default is true.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aAddr</td>
<td>       The address to which this UDP socket should be bound.  
</td>
</tr>

<tr>
<td>aAddressReuse</td>
<td>       If true, the socket is allowed to be bound to an address that is  
       already in use. Default is true.  
</td>
</tr>

</table>

### close() ###
<pre>  
close  
  
This method closes a UDP socket.  This does not affect already  
connected client sockets (i.e., the nsISocketTransport instances  
created from this UDP socket).  This will cause the onStopListening  
event to asynchronously fire with a status of NS_BINDING_ABORTED.  
  
</pre>
### asyncListen(aListener) ###
<pre>  
asyncListen  
  
This method puts the UDP socket in the listening state.  It will  
asynchronously listen for and accept client connections.  The listener  
will be notified once for each client connection that is accepted.  The  
listener's onSocketAccepted method will be called on the same thread  
that called asyncListen (the calling thread must have a nsIEventTarget).  
  
The listener will be passed a reference to an already connected socket  
transport (nsISocketTransport).  See below for more details.  
  
@param aListener  
       The listener to be notified when client connections are accepted.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>       The listener to be notified when client connections are accepted.  
</td>
</tr>

</table>

### getAddress() ###
<pre>  
Returns the address to which this UDP socket is bound.  Since a  
UDP socket may be bound to multiple network devices, this address  
may not necessarily be specific to a single network device.  In the  
case of an IP socket, the IP address field would be zerod out to  
indicate a UDP socket bound to all network devices.  Therefore,  
this method cannot be used to determine the IP address of the local  
system.  See nsIDNSService::myHostName if this is what you need.  
  
</pre>
### send(host, port, data, dataLength) ###
<pre>  
send  
  
Send out the datagram to specified remote host and port.  
DNS lookup will be triggered.  
  
@param host The remote host name.  
@param port The remote port.  
@param data The buffer containing the data to be written.  
@param dataLength The maximum number of bytes to be written.  
@return number of bytes written. (0 or dataLength)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>host</td>
<td>The remote host name.  
</td>
</tr>

<tr>
<td>port</td>
<td>The remote port.  
</td>
</tr>

<tr>
<td>data</td>
<td>The buffer containing the data to be written.  
</td>
</tr>

<tr>
<td>dataLength</td>
<td>The maximum number of bytes to be written.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>number of bytes written. (0 or dataLength)  
</td>
</tr>

</table>

### sendWithAddr(addr, data, dataLength) ###
<pre>  
sendWithAddr  
  
Send out the datagram to specified remote host and port.  
  
@param addr The remote host address.  
@param data The buffer containing the data to be written.  
@param dataLength The maximum number of bytes to be written.  
@return number of bytes written. (0 or dataLength)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>addr</td>
<td>The remote host address.  
</td>
</tr>

<tr>
<td>data</td>
<td>The buffer containing the data to be written.  
</td>
</tr>

<tr>
<td>dataLength</td>
<td>The maximum number of bytes to be written.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>number of bytes written. (0 or dataLength)  
</td>
</tr>

</table>

### sendWithAddress(addr, data, dataLength) ###
<pre>  
sendWithAddress  
  
Send out the datagram to specified remote address and port.  
  
@param addr The remote host address.  
@param data The buffer containing the data to be written.  
@param dataLength The maximum number of bytes to be written.  
@return number of bytes written. (0 or dataLength)  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>addr</td>
<td>The remote host address.  
</td>
</tr>

<tr>
<td>data</td>
<td>The buffer containing the data to be written.  
</td>
</tr>

<tr>
<td>dataLength</td>
<td>The maximum number of bytes to be written.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>number of bytes written. (0 or dataLength)  
</td>
</tr>

</table>

### sendBinaryStream(host, port, stream) ###
<pre>  
sendBinaryStream  
  
Send out the datagram to specified remote address and port.  
  
@param host The remote host name.  
@param port The remote port.  
@param stream The input stream to be sent. This must be a buffered stream implementation.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>host</td>
<td>The remote host name.  
</td>
</tr>

<tr>
<td>port</td>
<td>The remote port.  
</td>
</tr>

<tr>
<td>stream</td>
<td>The input stream to be sent. This must be a buffered stream implementation.  
</td>
</tr>

</table>

### sendBinaryStreamWithAddress(addr, stream) ###
<pre>  
sendBinaryStreamWithAddress  
  
Send out the datagram to specified remote address and port.  
  
@param addr The remote host address.  
@param stream The input stream to be sent. This must be a buffered stream implementation.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>addr</td>
<td>The remote host address.  
</td>
</tr>

<tr>
<td>stream</td>
<td>The input stream to be sent. This must be a buffered stream implementation.  
</td>
</tr>

</table>

### joinMulticast(addr, iface) ###
<pre>  
joinMulticast  
  
Join the multicast group specified by |addr|.  You are then able to  
receive future datagrams addressed to the group.  
  
@param addr  
       The multicast group address.  
@param iface  
       The local address of the interface on which to join the group.  If  
       this is not specified, the OS may join the group on all interfaces  
       or only the primary interface.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>addr</td>
<td>       The multicast group address.  
</td>
</tr>

<tr>
<td>iface</td>
<td>       The local address of the interface on which to join the group.  If  
       this is not specified, the OS may join the group on all interfaces  
       or only the primary interface.  
</td>
</tr>

</table>

### joinMulticastAddr(addr, iface) ###

### leaveMulticast(addr, iface) ###
<pre>  
leaveMulticast  
  
Leave the multicast group specified by |addr|.  You will no longer  
receive future datagrams addressed to the group.  
  
@param addr  
       The multicast group address.  
@param iface  
       The local address of the interface on which to leave the group.  
       If this is not specified, the OS may leave the group on all  
       interfaces or only the primary interface.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>addr</td>
<td>       The multicast group address.  
</td>
</tr>

<tr>
<td>iface</td>
<td>       The local address of the interface on which to leave the group.  
       If this is not specified, the OS may leave the group on all  
       interfaces or only the primary interface.  
</td>
</tr>

</table>

### leaveMulticastAddr(addr, iface) ###

## Attributes ##

### localAddr ###
<pre>  
Returns the local address of this UDP socket  
  
</pre>
### port ###
<pre>  
Returns the port of this UDP socket.  
  
</pre>
### multicastLoopback ###
<pre>  
multicastLoopback  
  
Whether multicast datagrams sent via this socket should be looped back to  
this host (assuming this host has joined the relevant group).  Defaults  
to true.  
Note: This is currently write-only.  
  
</pre>
### multicastInterface ###
<pre>  
multicastInterface  
  
The interface that should be used for sending future multicast datagrams.  
Note: This is currently write-only.  
  
</pre>
### multicastInterfaceAddr ###
<pre>  
multicastInterfaceAddr  
  
The interface that should be used for sending future multicast datagrams.  
Note: This is currently write-only.  
  
</pre>