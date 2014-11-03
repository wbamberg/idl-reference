---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/media/webspeech/synth/nsISpeechService.idl">Source file</a>
</div>

# nsISpeechTask #
<pre>  
A task is associated with a single utterance. It is provided by the browser  
to the service in the speak() method.  
  
</pre>
## Methods ##

### setup(aCallback, aChannels, aRate) ###
<pre>  
Prepare browser for speech.  
  
@param aCallback callback object for mid-speech operations.  
@param aChannels number of audio channels. Only required  
                   in direct audio services  
@param aRate     audio rate. Only required in direct audio services  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aCallback</td>
<td>callback object for mid-speech operations.  
</td>
</tr>

<tr>
<td>aChannels</td>
<td>number of audio channels. Only required  
                   in direct audio services  
</td>
</tr>

<tr>
<td>aRate</td>
<td>audio rate. Only required in direct audio services  
</td>
</tr>

</table>

### sendAudio(aData, aLandmarks) ###
<pre>  
Send audio data to browser.  
  
@param aData     an Int16Array with PCM-16 audio data.  
@param aLandmarks an array of sample offset and landmark pairs.  
                    Used for emiting boundary and mark events.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aData</td>
<td>an Int16Array with PCM-16 audio data.  
</td>
</tr>

<tr>
<td>aLandmarks</td>
<td>an array of sample offset and landmark pairs.  
                    Used for emiting boundary and mark events.  
</td>
</tr>

</table>

### sendAudioNative(aData, aDataLen) ###

### dispatchStart() ###
<pre>  
Dispatch start event.  
  
</pre>
### dispatchEnd(aElapsedTime, aCharIndex) ###
<pre>  
Dispatch end event.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aElapsedTime</td>
<td>time in seconds since speech has started.  
</td>
</tr>

<tr>
<td>aCharIndex</td>
<td>offset of spoken characters.  
</td>
</tr>

</table>

### dispatchPause(aElapsedTime, aCharIndex) ###
<pre>  
Dispatch pause event. Should not be called directly by service.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aElapsedTime</td>
<td>time in seconds since speech has started.  
</td>
</tr>

<tr>
<td>aCharIndex</td>
<td>offset of spoken characters.  
</td>
</tr>

</table>

### dispatchResume(aElapsedTime, aCharIndex) ###
<pre>  
Dispatch resume event. Should not be called directly by service.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aElapsedTime</td>
<td>time in seconds since speech has started.  
</td>
</tr>

<tr>
<td>aCharIndex</td>
<td>offset of spoken characters.  
</td>
</tr>

</table>

### dispatchError(aElapsedTime, aCharIndex) ###
<pre>  
Dispatch error event.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aElapsedTime</td>
<td>time in seconds since speech has started.  
</td>
</tr>

<tr>
<td>aCharIndex</td>
<td>offset of spoken characters.  
</td>
</tr>

</table>

### dispatchBoundary(aName, aElapsedTime, aCharIndex) ###
<pre>  
Dispatch boundary event.  
  
@param aName        name of boundary, 'word' or 'sentence'  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>name of boundary, 'word' or 'sentence'  
</td>
</tr>

<tr>
<td>aElapsedTime</td>
<td>time in seconds since speech has started.  
</td>
</tr>

<tr>
<td>aCharIndex</td>
<td>offset of spoken characters.  
</td>
</tr>

</table>

### dispatchMark(aName, aElapsedTime, aCharIndex) ###
<pre>  
Dispatch mark event.  
  
@param aName        mark identifier.  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>mark identifier.  
</td>
</tr>

<tr>
<td>aElapsedTime</td>
<td>time in seconds since speech has started.  
</td>
</tr>

<tr>
<td>aCharIndex</td>
<td>offset of spoken characters.  
</td>
</tr>

</table>
