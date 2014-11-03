---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/nfc/nsINfcContentHelper.idl">Source file</a>
</div>

# nsINfcContentHelper #

## Methods ##

### init(window) ###

### checkSessionToken(sessionToken) ###

### readNDEF(window, sessionToken) ###

### writeNDEF(window, records, sessionToken) ###

### makeReadOnlyNDEF(window, sessionToken) ###

### connect(window, techType, sessionToken) ###

### close(window, sessionToken) ###

### sendFile(window, blob, sessionToken) ###
  
Initiate Send file operation  
  
  
  
  
Returns DOMRequest, if initiation of send file operation is successful  
then 'onsuccess' is called else 'onerror'  
  

#### Parameters ####

<table>

<tr>
<td>window</td>
<td>       Current window  
</td>
</tr>

<tr>
<td>blob</td>
<td>       Raw data of the file to be sent. This object represents a file-like  
       (nsIDOMFile) object of immutable, raw data. The blob data needs  
       to be 'object wrapped' before calling this interface.  
</td>
</tr>

<tr>
<td>sessionToken</td>
<td>       Current token  
</td>
</tr>

</table>

### registerEventTarget(target) ###
  
Register the event target.  
  
  

#### Parameters ####

<table>

<tr>
<td>target</td>
<td>An instance of the nsINfcDOMEventTarget.  
</td>
</tr>

</table>

### registerTargetForPeerReady(window, appId) ###
  
Register the given application id with Chrome process  
  
  
  

#### Parameters ####

<table>

<tr>
<td>window</td>
<td>       Current window  
</td>
</tr>

<tr>
<td>appId</td>
<td>       Application ID to be registered  
</td>
</tr>

</table>

### unregisterTargetForPeerReady(window, appId) ###
  
Unregister the given application id with Chrome process  
  
  
  

#### Parameters ####

<table>

<tr>
<td>window</td>
<td>       Current window  
</td>
</tr>

<tr>
<td>appId</td>
<td>       Application ID to be registered  
</td>
</tr>

</table>

### checkP2PRegistration(window, appId) ###
  
Checks if the given application's id is a registered peer target (with the Chrome process)  
  
  
  
Returns DOMRequest, if appId is registered then 'onsuccess' is called else 'onerror'  
  

#### Parameters ####

<table>

<tr>
<td>window</td>
<td>       Current window  
</td>
</tr>

<tr>
<td>appId</td>
<td>       Application ID to be updated with Chrome process  
</td>
</tr>

</table>

### notifyUserAcceptedP2P(window, appId) ###
  
Notify the Chrome process that user has accepted to share nfc message on P2P UI  
  
  
  

#### Parameters ####

<table>

<tr>
<td>window</td>
<td>       Current window  
</td>
</tr>

<tr>
<td>appId</td>
<td>       Application ID that is capable of handling NFC_EVENT_PEER_READY event  
</td>
</tr>

</table>

### notifySendFileStatus(window, status, requestId) ###
  
Notify the status of sendFile operation to Chrome process  
  
  
  
  

#### Parameters ####

<table>

<tr>
<td>window</td>
<td>       Current window  
</td>
</tr>

<tr>
<td>status</td>
<td>       Status of sendFile operation  
</td>
</tr>

<tr>
<td>requestId</td>
<td>       Request ID of SendFile DOM Request  
</td>
</tr>

</table>

### startPoll(window) ###
  
Power on the NFC hardware and start polling for NFC tags or devices.  
  

### stopPoll(window) ###
  
Stop polling for NFC tags or devices. i.e. enter low power mode.  
  

### powerOff(window) ###
  
Power off the NFC hardware.  
  

## Constants ##

### NFC_EVENT_PEER_READY ###

### NFC_EVENT_PEER_LOST ###
