---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/audiochannel/nsIAudioChannelAgent.idl">Source file</a>
</div>

# nsIAudioChannelAgentCallback #

## Methods ##

### canPlayChanged(canPlay) ###
  
Notified when the playable status of channel is changed.  
  
@param canPlay  
       Callback from agent to notify component of the playable status  
       of the channel. If canPlay is muted state, component SHOULD stop  
       playing media associated with this channel as soon as possible. if  
       it is faded state then the volume of media should be reduced.  
  

#### Parameters ####

<table>

<tr>
<td>canPlay</td>
<td>       Callback from agent to notify component of the playable status  
       of the channel. If canPlay is muted state, component SHOULD stop  
       playing media associated with this channel as soon as possible. if  
       it is faded state then the volume of media should be reduced.  
</td>
</tr>

</table>

### windowVolumeChanged() ###
  
Notified when the window volume/mute is changed  
  
