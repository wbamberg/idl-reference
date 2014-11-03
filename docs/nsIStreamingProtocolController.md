---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIStreamingProtocolController.idl">Source file</a>
</div>

# nsIStreamingProtocolController #
<pre>  
Media stream controller API: control and retrieve meta data from media stream.  
  
</pre>
## Methods ##

### init(aUri) ###
<pre>  
Preprare the URI before we can start the connection.  
@param aUri The URI of the media stream.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aUri</td>
<td>The URI of the media stream.  
</td>
</tr>

</table>

### asyncOpen(aListener) ###
<pre>  
Asynchronously open this controller.  Data is fed to the specified  
media stream listener as it becomes available. If asyncOpen returns  
successfully, the controller is responsible for keeping itself alive  
until it has called onStopRequest on aListener.  
  
@param aListener The nsIStreamingProtocolListener implementation  
  
</pre>
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
<pre>  
Total number of audio/video tracks.  
  
</pre>