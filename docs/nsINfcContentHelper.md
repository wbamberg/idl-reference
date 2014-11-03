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
<code>  
Initiate Send file operation  
  
@param window  
       Current window  
  
@param blob  
       Raw data of the file to be sent. This object represents a file-like  
       (nsIDOMFile) object of immutable, raw data. The blob data needs  
       to be 'object wrapped' before calling this interface.  
  
@param sessionToken  
       Current token  
  
Returns DOMRequest, if initiation of send file operation is successful  
then 'onsuccess' is called else 'onerror'  
  
</code>
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
<code>  
Register the event target.  
  
@param target  An instance of the nsINfcDOMEventTarget.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>target</td>
<td>An instance of the nsINfcDOMEventTarget.  
</td>
</tr>

</table>

### registerTargetForPeerReady(window, appId) ###
<code>  
Register the given application id with Chrome process  
  
@param window  
       Current window  
  
@param appId  
       Application ID to be registered  
  
</code>
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
<code>  
Unregister the given application id with Chrome process  
  
@param window  
       Current window  
  
@param appId  
       Application ID to be registered  
  
</code>
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
<code>  
Checks if the given application's id is a registered peer target (with the Chrome process)  
  
@param window  
       Current window  
  
@param appId  
       Application ID to be updated with Chrome process  
  
Returns DOMRequest, if appId is registered then 'onsuccess' is called else 'onerror'  
  
</code>
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
<code>  
Notify the Chrome process that user has accepted to share nfc message on P2P UI  
  
@param window  
       Current window  
  
@param appId  
       Application ID that is capable of handling NFC_EVENT_PEER_READY event  
  
</code>
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
<code>  
Notify the status of sendFile operation to Chrome process  
  
@param window  
       Current window  
  
@param status  
       Status of sendFile operation  
  
@param requestId  
       Request ID of SendFile DOM Request  
  
</code>
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
<code>  
Power on the NFC hardware and start polling for NFC tags or devices.  
  
</code>
### stopPoll(window) ###
<code>  
Stop polling for NFC tags or devices. i.e. enter low power mode.  
  
</code>
### powerOff(window) ###
<code>  
Power off the NFC hardware.  
  
</code>
## Constants ##

### NFC_EVENT_PEER_READY ###

### NFC_EVENT_PEER_LOST ###
