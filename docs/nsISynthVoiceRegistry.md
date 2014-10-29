---
layout: default
---

# nsISynthVoiceRegistry #

## Methods ##

### addVoice ###

Register a speech synthesis voice.

@param aService      the service that provides this voice.
@param aUri          a unique identifier for this voice.
@param aName         human-readable name for this voice.
@param aLang         a BCP 47 language tag.
@param aLocalService true if service does not require network.


### removeVoice ###

Remove a speech synthesis voice.

@param aService the service that was used to add the voice.
@param aUri     a unique identifier of an existing voice.


### setDefaultVoice ###

Set a voice as default.

@param aUri       a unique identifier of an existing voice.
@param aIsDefault true if this voice should be toggled as default.


### getVoice ###

### isDefaultVoice ###

### isLocalVoice ###

### getVoiceLang ###

### getVoiceName ###

## Attributes ##

### voiceCount ###
