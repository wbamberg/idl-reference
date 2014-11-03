---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIStreamingProtocolController.idl">Source file</a>
</div>

# nsIStreamingProtocolListener #
  
nsIStreamingProtocolListener  
  

## Methods ##

### onMediaDataAvailable(index, data, length, offset, meta) ###
  
Called when the data may be read without blocking the calling thread.  
@param index The track number of the media stream.  
@param data Raw data of the media stream on given track number.  
@param length The length of the raw data.  
@param offset The offset in the data stream from the start of the media  
              presentation in bytes.  
@param meta The meta data of the frame.  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The track number of the media stream.  
</td>
</tr>

<tr>
<td>data</td>
<td>Raw data of the media stream on given track number.  
</td>
</tr>

<tr>
<td>length</td>
<td>The length of the raw data.  
</td>
</tr>

<tr>
<td>offset</td>
<td>The offset in the data stream from the start of the media  
              presentation in bytes.  
</td>
</tr>

<tr>
<td>meta</td>
<td>The meta data of the frame.  
</td>
</tr>

</table>

### onConnected(index, meta) ###
  
Called when the meta data for a given session is available.  
@param index The track number of the media stream.  
@param meta The meta data of the media stream.  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The track number of the media stream.  
</td>
</tr>

<tr>
<td>meta</td>
<td>The meta data of the media stream.  
</td>
</tr>

</table>

### onDisconnected(index, reason) ###
  
Called when the Rtsp session is closed.  
@param index Track number of the media stream.  
@param reason The reason of disconnection.  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>Track number of the media stream.  
</td>
</tr>

<tr>
<td>reason</td>
<td>The reason of disconnection.  
</td>
</tr>

</table>
