---
layout: default
---

# nsISpeechService #
  
The main interface of a speech synthesis service.  
  
A service's speak method could be implemented in two ways:  
 1. Indirect audio - the service is responsible for outputting audio.  
   The service calls the nsISpeechTask.dispatch* methods directly. Starting  
   with dispatchStart() and ending with dispatchEnd or dispatchError().  
  
 2. Direct audio - the service provides us with PCM-16 data, and we output it.  
   The service does not call the dispatch task methods directly. Instead,  
   audio information is provided at setup(), and audio data is sent with  
   sendAudio(). The utterance is terminated with an empty sendAudio().  
  

## Methods ##

### speak ###
  
Speak the given text using the voice identified byu the given uri. See  
W3C Speech API spec for information about pitch and rate.  
https://dvcs.w3.org/hg/speech-api/raw-file/tip/speechapi.html#utterance-attributes  
  
@param aText  text to utter.  
@param aUri   unique voice identifier.  
@param aRate  rate to speak voice in.  
@param aPitch pitch to speak voice in.  
@param aTask  task instance for utterance, used for sending events or audio  
                data back to browser.  
  

## Attributes ##

### serviceType ###

## Constants ##

### SERVICETYPE_DIRECT_AUDIO ###

### SERVICETYPE_INDIRECT_AUDIO ###
