---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/system/gonk/nsIAudioManager.idl">Source file</a>
</div>
# nsIAudioManager #

## Methods ##

### setForceForUse(usage, force) ###

### getForceForUse(usage) ###

### setAudioChannelVolume(channel, index) ###

### getAudioChannelVolume(channel) ###

### getMaxAudioChannelVolume(channel) ###

## Attributes ##

### microphoneMuted ###
  
Microphone muted?  
  

### fmRadioAudioEnabled ###
  
Are we playing audio from the FM radio?  
  

### phoneState ###

## Constants ##

### PHONE_STATE_INVALID ###
  
Set the phone's audio mode.  
  

### PHONE_STATE_CURRENT ###

### PHONE_STATE_NORMAL ###

### PHONE_STATE_RINGTONE ###

### PHONE_STATE_IN_CALL ###

### PHONE_STATE_IN_COMMUNICATION ###

### FORCE_NONE ###
  
Configure a particular device ("force") to be used for one of the uses  
(communication, media playback, etc.)  
  

### FORCE_SPEAKER ###

### FORCE_HEADPHONES ###

### FORCE_BT_SCO ###

### FORCE_BT_A2DP ###

### FORCE_WIRED_ACCESSORY ###

### FORCE_BT_CAR_DOCK ###

### FORCE_BT_DESK_DOCK ###

### FORCE_ANALOG_DOCK ###

### FORCE_DIGITAL_DOCK ###

### FORCE_NO_BT_A2DP ###

### USE_COMMUNICATION ###

### USE_MEDIA ###

### USE_RECORD ###

### USE_DOCK ###
