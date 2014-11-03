---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsISocketTransport.idl">Source file</a>
</div>

# nsISocketTransport #
<pre>  
nsISocketTransport  
  
NOTE: Connection setup is triggered by opening an input or output stream,  
it does not start on its own. Completion of the connection setup is  
indicated by a STATUS_CONNECTED_TO notification to the event sink (if set).  
  
NOTE: This is a free-threaded interface, meaning that the methods on  
this interface may be called from any thread.  
  
</pre>
## Methods ##

### getPeerAddr() ###
<pre>  
Returns the IP address of the socket connection peer. This  
attribute is defined only once a connection has been established.  
  
</pre>
### getSelfAddr() ###
<pre>  
Returns the IP address of the initiating end. This attribute  
is defined only once a connection has been established.  
  
</pre>
### bind(aLocalAddr) ###
<pre>  
Bind to a specific local address.  
  
</pre>
### getScriptablePeerAddr() ###
<pre>  
Returns a scriptable version of getPeerAddr. This attribute is defined  
only once a connection has been established.  
  
</pre>
### getScriptableSelfAddr() ###
<pre>  
Returns a scriptable version of getSelfAddr. This attribute is defined  
only once a connection has been established.  
  
</pre>
### isAlive() ###
<pre>  
Test if this socket transport is (still) connected.  
  
</pre>
### getTimeout(aType) ###
<pre>  
Socket timeouts in seconds.  To specify no timeout, pass UINT32_MAX  
as aValue to setTimeout.  The implementation may truncate timeout values  
to a smaller range of values (e.g., 0 to 0xFFFF).  
  
</pre>
### setTimeout(aType, aValue) ###

### setKeepaliveVals(keepaliveIdleTime, keepaliveRetryInterval) ###

## Attributes ##

### host ###
<pre>  
Get the peer's host for the underlying socket connection.  
For Unix domain sockets, this is a pathname, or the empty string for  
unnamed and abstract socket addresses.  
  
</pre>
### port ###
<pre>  
Get the port for the underlying socket connection.  
For Unix domain sockets, this is zero.  
  
</pre>
### securityInfo ###
<pre>  
Security info object returned from the secure socket provider.  This  
object supports nsISSLSocketControl, nsITransportSecurityInfo, and  
possibly other interfaces.  
  
This attribute is only available once the socket is connected.  
  
</pre>
### securityCallbacks ###
<pre>  
Security notification callbacks passed to the secure socket provider  
via nsISSLSocketControl at socket creation time.  
  
NOTE: this attribute cannot be changed once a stream has been opened.  
  
</pre>
### connectionFlags ###
<pre>  
connectionFlags is a bitmask that can be used to modify underlying   
behavior of the socket connection. See the flags below.  
  
</pre>
### QoSBits ###
<pre>  
Socket QoS/ToS markings. Valid values are IPTOS_DSCP_AFxx or  
IPTOS_CLASS_CSx (or IPTOS_DSCP_EF, but currently no supported  
services require expedited-forwarding).  
Not setting this value will leave the socket with the default  
ToS value, which on most systems if IPTOS_CLASS_CS0 (formerly  
IPTOS_PREC_ROUTINE).  
  
</pre>
### recvBufferSize ###
<pre>  
TCP send and receive buffer sizes. A value of 0 means OS level  
auto-tuning is in effect.  
  
</pre>
### sendBufferSize ###

### keepaliveEnabled ###
<pre>  
TCP keepalive configuration (support varies by platform).  
  
</pre>
## Constants ##

### TIMEOUT_CONNECT ###
<pre>  
Values for the aType parameter passed to get/setTimeout.  
  
</pre>
### TIMEOUT_READ_WRITE ###

### STATUS_RESOLVING ###
<pre>  
nsITransportEventSink status codes.  
  
Although these look like XPCOM error codes and are passed in an nsresult  
variable, they are *not* error codes.  Note that while they *do* overlap  
with existing error codes in Necko, these status codes are confined  
within a very limited context where no error codes may appear, so there  
is no ambiguity.  
  
The values of these status codes must never change.  
  
The status codes appear in near-chronological order (not in numeric  
order).  STATUS_RESOLVING may be skipped if the host does not need to be  
resolved.  STATUS_WAITING_FOR is an optional status code, which the impl  
of this interface may choose not to generate.  
  
In C++, these constants have a type of uint32_t, so C++ callers must use  
the NS_NET_STATUS_* constants defined below, which have a type of  
nsresult.  
  
</pre>
### STATUS_RESOLVED ###

### STATUS_CONNECTING_TO ###

### STATUS_CONNECTED_TO ###

### STATUS_SENDING_TO ###

### STATUS_WAITING_FOR ###

### STATUS_RECEIVING_FROM ###

### BYPASS_CACHE ###
<pre>  
Values for the connectionFlags  
  
When making a new connection BYPASS_CACHE will force the Necko DNS   
cache entry to be refreshed with a new call to NSPR if it is set before  
opening the new stream.  
  
</pre>
### ANONYMOUS_CONNECT ###
<pre>  
When setting this flag, the socket will not apply any  
credentials when establishing a connection. For example,  
an SSL connection would not send any client-certificates  
if this flag is set.  
  
</pre>
### DISABLE_IPV6 ###
<pre>  
If set, we will skip all IPv6 addresses the host may have and only  
connect to IPv4 ones.  
  
</pre>
### NO_PERMANENT_STORAGE ###
<pre>  
If set, indicates that the connection was initiated from a source  
defined as being private in the sense of Private Browsing. Generally,  
there should be no state shared between connections that are private  
and those that are not; it is OK for multiple private connections  
to share state with each other, and it is OK for multiple non-private  
connections to share state with each other.  
  
</pre>
### DISABLE_IPV4 ###
<pre>  
If set, we will skip all IPv4 addresses the host may have and only  
connect to IPv6 ones.  
  
</pre>
### DISABLE_RFC1918 ###
<pre>  
If set, indicates that the socket should not connect if the hostname  
resolves to an RFC1918 address or IPv6 equivalent.  
  
</pre>