---
layout: default
---

# nsISpeechTask #
  
A task is associated with a single utterance. It is provided by the browser  
to the service in the speak() method.  
  

## Methods ##

### setup ###
  
Prepare browser for speech.  
  
@param aCallback callback object for mid-speech operations.  
@param aChannels number of audio channels. Only required  
                   in direct audio services  
@param aRate     audio rate. Only required in direct audio services  
  

### sendAudio ###
  
Send audio data to browser.  
  
@param aData     an Int16Array with PCM-16 audio data.  
@param aLandmarks an array of sample offset and landmark pairs.  
                    Used for emiting boundary and mark events.  
  

### sendAudioNative ###

### dispatchStart ###
  
Dispatch start event.  
  

### dispatchEnd ###
  
Dispatch end event.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  

### dispatchPause ###
  
Dispatch pause event. Should not be called directly by service.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  

### dispatchResume ###
  
Dispatch resume event. Should not be called directly by service.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  

### dispatchError ###
  
Dispatch error event.  
  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  

### dispatchBoundary ###
  
Dispatch boundary event.  
  
@param aName        name of boundary, 'word' or 'sentence'  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  

### dispatchMark ###
  
Dispatch mark event.  
  
@param aName        mark identifier.  
@param aElapsedTime time in seconds since speech has started.  
@param aCharIndex   offset of spoken characters.  
  
