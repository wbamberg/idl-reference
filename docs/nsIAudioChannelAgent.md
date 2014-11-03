---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/audiochannel/nsIAudioChannelAgent.idl">Source file</a>
</div>

# nsIAudioChannelAgent #
<code>  
This interface provides an agent for gecko components to participate  
in the audio channel service. Gecko components are responsible for  
  1. Indicating what channel type they are using (via the init() member  
     function).  
  2. Before playing, checking the playable status of the channel.  
  3. Notifying the agent when they start/stop using this channel.  
  4. Notifying the agent of changes to the visibility of the component using  
     this channel.  
  
The agent will invoke a callback to notify Gecko components of  
  1. Changes to the playable status of this channel.  
  
</code>
## Methods ##

### init(window, channelType, callback) ###
<code>  
Initialize the agent with a channel type.  
Note: This function should only be called once.  
  
@param window  
   The window  
@param channelType  
   Audio Channel Type listed as above  
@param callback  
   1. Once the playable status changes, agent uses this callback function  
      to notify Gecko component.  
   2. The callback is allowed to be null. Ex: telephony doesn't need to  
      listen change of the playable status.  
   3. The AudioChannelAgent keeps a strong reference to the callback  
      object.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>window</td>
<td>   The window  
</td>
</tr>

<tr>
<td>channelType</td>
<td>   Audio Channel Type listed as above  
</td>
</tr>

<tr>
<td>callback</td>
<td>   1. Once the playable status changes, agent uses this callback function  
      to notify Gecko component.  
   2. The callback is allowed to be null. Ex: telephony doesn't need to  
      listen change of the playable status.  
   3. The AudioChannelAgent keeps a strong reference to the callback  
      object.  
</td>
</tr>

</table>

### initWithWeakCallback(window, channelType, callback) ###
<code>  
This method is just like init(), except the audio channel agent keeps a  
weak reference to the callback object.  
  
In order for this to work, |callback| must implement  
nsISupportsWeakReference.  
  
</code>
### initWithVideo(window, channelType, callback, weak) ###
<code>  
This method is just like init(), and specify the channel is associated  
with video.  
  
@param weak  
   true if weak reference should be hold.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>weak</td>
<td>   true if weak reference should be hold.  
</td>
</tr>

</table>

### startPlaying() ###
<code>  
Notify the agent that we want to start playing.  
Note: Gecko component SHOULD call this function first then start to  
         play audio stream only when return value is true.  
  
  
@return  
   normal state: the agent has registered with audio channel service and  
         the component should start playback.  
   muted state: the agent has registered with audio channel service but  
         the component should not start playback.  
   faded state: the agent has registered with audio channel service the  
         component should start playback as well as reducing the volume.  
  
</code>
#### Returns ####

<table>

<tr>
<td>   normal state: the agent has registered with audio channel service and  
         the component should start playback.  
   muted state: the agent has registered with audio channel service but  
         the component should not start playback.  
   faded state: the agent has registered with audio channel service the  
         component should start playback as well as reducing the volume.  
</td>
</tr>

</table>

### stopPlaying() ###
<code>  
Notify the agent we no longer want to play.  
  
Note : even if startPlaying() returned false, the agent would still be  
       registered with the audio channel service and receive callbacks for status changes.  
       So stopPlaying must still eventually be called to unregister the agent with the  
       channel service.  
  
</code>
### setVisibilityState(visible) ###
<code>  
Notify the agent of the visibility state of the window using this agent.  
@param visible  
   True if the window associated with the agent is visible.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>visible</td>
<td>   True if the window associated with the agent is visible.  
</td>
</tr>

</table>

## Attributes ##

### audioChannelType ###
  
Before init() is called, this returns AUDIO_AGENT_CHANNEL_ERROR.  
  

### windowVolume ###
  
Retrieve the volume from the window.  
  

## Constants ##

### AUDIO_AGENT_CHANNEL_NORMAL ###

### AUDIO_AGENT_CHANNEL_CONTENT ###

### AUDIO_AGENT_CHANNEL_NOTIFICATION ###

### AUDIO_AGENT_CHANNEL_ALARM ###

### AUDIO_AGENT_CHANNEL_TELEPHONY ###

### AUDIO_AGENT_CHANNEL_RINGER ###

### AUDIO_AGENT_CHANNEL_PUBLICNOTIFICATION ###

### AUDIO_AGENT_CHANNEL_ERROR ###

### AUDIO_AGENT_STATE_NORMAL ###

### AUDIO_AGENT_STATE_MUTED ###

### AUDIO_AGENT_STATE_FADED ###
