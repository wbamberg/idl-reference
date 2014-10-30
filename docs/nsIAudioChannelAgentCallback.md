---
layout: default
---

# nsIAudioChannelAgentCallback #

## Methods ##

### canPlayChanged ###
  
Notified when the playable status of channel is changed.  
  
@param canPlay  
       Callback from agent to notify component of the playable status  
       of the channel. If canPlay is muted state, component SHOULD stop  
       playing media associated with this channel as soon as possible. if  
       it is faded state then the volume of media should be reduced.  
  

### windowVolumeChanged ###
  
Notified when the window volume/mute is changed  
  
