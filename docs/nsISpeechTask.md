---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/media/webspeech/synth/nsISpeechService.idl">Source file</a>
</div>

# nsISpeechTask #
  
A task is associated with a single utterance. It is provided by the browser  
to the service in the speak() method.  
  

## Methods ##

### setup(aCallback, aChannels, aRate) ###
  
Prepare browser for speech.  
  
  

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
  
Send audio data to browser.  
  
  

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
  
Dispatch start event.  
  

### dispatchEnd(aElapsedTime, aCharIndex) ###
  
Dispatch end event.  
  
  

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
  
Dispatch pause event. Should not be called directly by service.  
  
  

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
  
Dispatch resume event. Should not be called directly by service.  
  
  

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
  
Dispatch error event.  
  
  

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
  
Dispatch boundary event.  
  
  

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
  
Dispatch mark event.  
  
  

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
