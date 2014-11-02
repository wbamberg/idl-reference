---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIStreamingProtocolController.idl">Source file</a>
</div>
# nsIStreamingProtocolController #
  
Media stream controller API: control and retrieve meta data from media stream.  
  

## Methods ##

### init(aUri) ###
  
Preprare the URI before we can start the connection.  
@param aUri The URI of the media stream.  
  

#### Parameters ####

<table>

<tr>
<td>aUri</td>
<td>The URI of the media stream.  
</td>
</tr>

</table>

### asyncOpen(aListener) ###
  
Asynchronously open this controller.  Data is fed to the specified  
media stream listener as it becomes available. If asyncOpen returns  
successfully, the controller is responsible for keeping itself alive  
until it has called onStopRequest on aListener.  
  
@param aListener The nsIStreamingProtocolListener implementation  
  

#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>The nsIStreamingProtocolListener implementation  
</td>
</tr>

</table>

### getTrackMetaData(index) ###

### play() ###

### pause() ###

### resume() ###

### suspend() ###

### seek(seekTimeUs) ###

### stop() ###

### playbackEnded() ###

## Attributes ##

### totalTracks ###
  
Total number of audio/video tracks.  
  
