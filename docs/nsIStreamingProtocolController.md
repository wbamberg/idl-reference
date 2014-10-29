---
layout: default
---

# nsIStreamingProtocolController #

Media stream controller API: control and retrieve meta data from media stream.


## Methods ##

### init ###

Preprare the URI before we can start the connection.
@param aUri The URI of the media stream.


### asyncOpen ###

Asynchronously open this controller.  Data is fed to the specified
media stream listener as it becomes available. If asyncOpen returns
successfully, the controller is responsible for keeping itself alive
until it has called onStopRequest on aListener.

@param aListener The nsIStreamingProtocolListener implementation


### getTrackMetaData ###

### play ###

### pause ###

### resume ###

### suspend ###

### seek ###

### stop ###

### playbackEnded ###

## Attributes ##

### totalTracks ###

Total number of audio/video tracks.

