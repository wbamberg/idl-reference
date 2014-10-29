---
layout: default
---

# nsIWapPushApplication #

Handle WAP Push notifications.


## Methods ##

### receiveWapPush ###

Receive WAP Push message.

@param aData
       An array containing raw PDU data.
@param aLength
       Length of aData.
@param aOffset
       Start offset of aData containing message body of the Push PDU.
@param options
       An object containing various attributes from lower transport layer.

