---
layout: default
---

# nsIWebSocketListener #

nsIWebSocketListener: passed to nsIWebSocketChannel::AsyncOpen. Receives
websocket traffic events as they arrive.


## Methods ##

### onStart ###

Called to signify the establishment of the message stream.

Unlike most other networking channels (which use nsIRequestObserver
instead of this class), we do not guarantee that OnStart is always
called: OnStop is called without calling this function if errors occur
during connection setup.  If the websocket connection is successful,
OnStart will be called before any other calls to this API.

@param aContext user defined context


### onStop ###

Called to signify the completion of the message stream.
OnStop is the final notification the listener will receive and it
completes the WebSocket connection: after it returns the
nsIWebSocketChannel will release its reference to the listener.

Note: this event can be received in error cases even if
nsIWebSocketChannel::Close() has not been called.

@param aContext user defined context
@param aStatusCode reason for stopping (NS_OK if completed successfully)


### onMessageAvailable ###

Called to deliver text message.

@param aContext user defined context
@param aMsg the message data


### onBinaryMessageAvailable ###

Called to deliver binary message.

@param aContext user defined context
@param aMsg the message data


### onAcknowledge ###

Called to acknowledge message sent via sendMsg() or sendBinaryMsg.

@param aContext user defined context
@param aSize number of bytes placed in OS send buffer


### onServerClose ###

Called to inform receipt of WebSocket Close message from server.
In the case of errors onStop() can be called without ever
receiving server close.

No additional messages through onMessageAvailable(),
onBinaryMessageAvailable() or onAcknowledge() will be delievered
to the listener after onServerClose(), though outgoing messages can still
be sent through the nsIWebSocketChannel connection.

@param aContext user defined context
@param aCode the websocket closing handshake close code.
@param aReason the websocket closing handshake close reason


