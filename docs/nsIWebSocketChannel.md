---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/websocket/nsIWebSocketChannel.idl">Source file</a>
</div>

# nsIWebSocketChannel #
<pre>  
Low-level websocket API: handles network protocol.    
  
This is primarly intended for use by the higher-level nsIWebSocket.idl.  
We are also making it scriptable for now, but this may change once we have  
WebSockets for Workers.  
  
</pre>
## Methods ##

### asyncOpen(aURI, aOrigin, aListener, aContext) ###
<pre>  
Asynchronously open the websocket connection.  Received messages are fed  
to the socket listener as they arrive.  The socket listener's methods  
are called on the thread that calls asyncOpen and are not called until  
after asyncOpen returns.  If asyncOpen returns successfully, the  
protocol implementation promises to call at least onStop on the listener.  
  
NOTE: Implementations should throw NS_ERROR_ALREADY_OPENED if the  
websocket connection is reopened.  
  
@param aURI the uri of the websocket protocol - may be redirected  
@param aOrigin the uri of the originating resource  
@param aListener the nsIWebSocketListener implementation  
@param aContext an opaque parameter forwarded to aListener's methods  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the uri of the websocket protocol - may be redirected  
</td>
</tr>

<tr>
<td>aOrigin</td>
<td>the uri of the originating resource  
</td>
</tr>

<tr>
<td>aListener</td>
<td>the nsIWebSocketListener implementation  
</td>
</tr>

<tr>
<td>aContext</td>
<td>an opaque parameter forwarded to aListener's methods  
</td>
</tr>

</table>

### close(aCode, aReason) ###

### sendMsg(aMsg) ###
<pre>  
Use to send text message down the connection to WebSocket peer.  
  
@param aMsg the utf8 string to send  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aMsg</td>
<td>the utf8 string to send  
</td>
</tr>

</table>

### sendBinaryMsg(aMsg) ###
<pre>  
Use to send binary message down the connection to WebSocket peer.  
  
@param aMsg the data to send  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aMsg</td>
<td>the data to send  
</td>
</tr>

</table>

### sendBinaryStream(aStream, length) ###
<pre>   
Use to send a binary stream (Blob) to Websocket peer.  
  
@param aStream The input stream to be sent.    
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>The input stream to be sent.    
</td>
</tr>

</table>

## Attributes ##

### originalURI ###
<pre>  
The original URI used to construct the protocol connection. This is used  
in the case of a redirect or URI "resolution" (e.g. resolving a  
resource: URI to a file: URI) so that the original pre-redirect  
URI can still be obtained.  This is never null.  
  
</pre>
### URI ###
<pre>  
The readonly URI corresponding to the protocol connection after any  
redirections are completed.  
  
</pre>
### notificationCallbacks ###
<pre>  
The notification callbacks for authorization, etc..  
  
</pre>
### securityInfo ###
<pre>  
Transport-level security information (if any)  
  
</pre>
### loadGroup ###
<pre>  
The load group of of the websocket  
  
</pre>
### loadInfo ###
<pre>  
The load info of the websocket  
  
</pre>
### protocol ###
<pre>  
Sec-Websocket-Protocol value  
  
</pre>
### extensions ###
<pre>  
Sec-Websocket-Extensions response header value  
  
</pre>
### pingInterval ###
<pre>  
This value determines how often (in seconds) websocket keepalive  
pings are sent.  If set to 0 (the default), no pings are ever sent.  
  
This value can currently only be set before asyncOpen is called, else   
NS_ERROR_IN_PROGRESS is thrown.  
  
Be careful using this setting: ping traffic can consume lots of power and  
bandwidth over time.  
  
</pre>
### pingTimeout ###
<pre>  
This value determines how long (in seconds) the websocket waits for  
the server to reply to a ping that has been sent before considering the  
connection broken.  
  
This value can currently only be set before asyncOpen is called, else   
NS_ERROR_IN_PROGRESS is thrown.  
  
</pre>
## Constants ##

### CLOSE_NORMAL ###

### CLOSE_GOING_AWAY ###

### CLOSE_PROTOCOL_ERROR ###

### CLOSE_UNSUPPORTED_DATATYPE ###

### CLOSE_NO_STATUS ###

### CLOSE_ABNORMAL ###

### CLOSE_INVALID_PAYLOAD ###

### CLOSE_POLICY_VIOLATION ###

### CLOSE_TOO_LARGE ###

### CLOSE_EXTENSION_MISSING ###

### CLOSE_INTERNAL_ERROR ###

### CLOSE_TLS_FAILED ###
