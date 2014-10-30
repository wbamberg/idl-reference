---
layout: default
---

# nsISynthVoiceRegistry #

## Methods ##

### addVoice(aService, aUri, aName, aLang, aLocalService) ###
  
Register a speech synthesis voice.  
  
@param aService      the service that provides this voice.  
@param aUri          a unique identifier for this voice.  
@param aName         human-readable name for this voice.  
@param aLang         a BCP 47 language tag.  
@param aLocalService true if service does not require network.  
  

### removeVoice(aService, aUri) ###
  
Remove a speech synthesis voice.  
  
@param aService the service that was used to add the voice.  
@param aUri     a unique identifier of an existing voice.  
  

### setDefaultVoice(aUri, aIsDefault) ###
  
Set a voice as default.  
  
@param aUri       a unique identifier of an existing voice.  
@param aIsDefault true if this voice should be toggled as default.  
  

### getVoice(aIndex) ###

### isDefaultVoice(aUri) ###

### isLocalVoice(aUri) ###

### getVoiceLang(aUri) ###

### getVoiceName(aUri) ###

## Attributes ##

### voiceCount ###
