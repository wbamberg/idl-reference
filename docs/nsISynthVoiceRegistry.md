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
  

#### Parameters ####

<table>

<tr>
<td>aService</td>
<td>the service that provides this voice.  
</td>
</tr>

<tr>
<td>aService</td>
<td>the service that provides this voice.  
</td>
</tr>

<tr>
<td>aService</td>
<td>the service that provides this voice.  
</td>
</tr>

<tr>
<td>aService</td>
<td>the service that provides this voice.  
</td>
</tr>

<tr>
<td>aService</td>
<td>the service that provides this voice.  
</td>
</tr>

</table>

### removeVoice(aService, aUri) ###
  
Remove a speech synthesis voice.  
  
@param aService the service that was used to add the voice.  
@param aUri     a unique identifier of an existing voice.  
  

#### Parameters ####

<table>

<tr>
<td>aService</td>
<td>the service that was used to add the voice.  
</td>
</tr>

<tr>
<td>aService</td>
<td>the service that was used to add the voice.  
</td>
</tr>

</table>

### setDefaultVoice(aUri, aIsDefault) ###
  
Set a voice as default.  
  
@param aUri       a unique identifier of an existing voice.  
@param aIsDefault true if this voice should be toggled as default.  
  

#### Parameters ####

<table>

<tr>
<td>aUri</td>
<td>a unique identifier of an existing voice.  
</td>
</tr>

<tr>
<td>aUri</td>
<td>a unique identifier of an existing voice.  
</td>
</tr>

</table>

### getVoice(aIndex) ###

### isDefaultVoice(aUri) ###

### isLocalVoice(aUri) ###

### getVoiceLang(aUri) ###

### getVoiceName(aUri) ###

## Attributes ##

### voiceCount ###
