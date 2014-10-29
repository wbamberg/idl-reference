---
layout: default
---

# nsIStreamingProtocolListener #

nsIStreamingProtocolListener


## Methods ##

### onMediaDataAvailable ###

Called when the data may be read without blocking the calling thread.
@param index The track number of the media stream.
@param data Raw data of the media stream on given track number.
@param length The length of the raw data.
@param offset The offset in the data stream from the start of the media
              presentation in bytes.
@param meta The meta data of the frame.


### onConnected ###

Called when the meta data for a given session is available.
@param index The track number of the media stream.
@param meta The meta data of the media stream.


### onDisconnected ###

Called when the Rtsp session is closed.
@param index Track number of the media stream.
@param reason The reason of disconnection.

