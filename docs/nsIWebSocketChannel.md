---
layout: default
---

# nsIWebSocketChannel #
  
Low-level websocket API: handles network protocol.    
  
This is primarly intended for use by the higher-level nsIWebSocket.idl.  
We are also making it scriptable for now, but this may change once we have  
WebSockets for Workers.  
  

## Methods ##

### asyncOpen(aURI, aOrigin, aListener, aContext) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>the uri of the websocket protocol - may be redirected  
</td>
</tr>

<tr>
<td>aURI</td>
<td>the uri of the websocket protocol - may be redirected  
</td>
</tr>

<tr>
<td>aURI</td>
<td>the uri of the websocket protocol - may be redirected  
</td>
</tr>

<tr>
<td>aURI</td>
<td>the uri of the websocket protocol - may be redirected  
</td>
</tr>

</table>

### close(aCode, aReason) ###

### sendMsg(aMsg) ###
  
Use to send text message down the connection to WebSocket peer.  
  
@param aMsg the utf8 string to send  
  

#### Parameters ####

<table>

<tr>
<td>aMsg</td>
<td>the utf8 string to send  
</td>
</tr>

</table>

### sendBinaryMsg(aMsg) ###
  
Use to send binary message down the connection to WebSocket peer.  
  
@param aMsg the data to send  
  

#### Parameters ####

<table>

<tr>
<td>aMsg</td>
<td>the data to send  
</td>
</tr>

</table>

### sendBinaryStream(aStream, length) ###
   
Use to send a binary stream (Blob) to Websocket peer.  
  
@param aStream The input stream to be sent.    
  

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
  
The original URI used to construct the protocol connection. This is used  
in the case of a redirect or URI "resolution" (e.g. resolving a  
resource: URI to a file: URI) so that the original pre-redirect  
URI can still be obtained.  This is never null.  
  

### URI ###
  
The readonly URI corresponding to the protocol connection after any  
redirections are completed.  
  

### notificationCallbacks ###
  
The notification callbacks for authorization, etc..  
  

### securityInfo ###
  
Transport-level security information (if any)  
  

### loadGroup ###
  
The load group of of the websocket  
  

### loadInfo ###
  
The load info of the websocket  
  

### protocol ###
  
Sec-Websocket-Protocol value  
  

### extensions ###
  
Sec-Websocket-Extensions response header value  
  

### pingInterval ###
  
This value determines how often (in seconds) websocket keepalive  
pings are sent.  If set to 0 (the default), no pings are ever sent.  
  
This value can currently only be set before asyncOpen is called, else   
NS_ERROR_IN_PROGRESS is thrown.  
  
Be careful using this setting: ping traffic can consume lots of power and  
bandwidth over time.  
  

### pingTimeout ###
  
This value determines how long (in seconds) the websocket waits for  
the server to reply to a ping that has been sent before considering the  
connection broken.  
  
This value can currently only be set before asyncOpen is called, else   
NS_ERROR_IN_PROGRESS is thrown.  
  

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
