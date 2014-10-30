---
layout: default
---

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
  

### registerEventTarget(target) ###
  
Register the event target.  
  
@param target  An instance of the nsINfcDOMEventTarget.  
  

### registerTargetForPeerReady(window, appId) ###
  
Register the given application id with Chrome process  
  
@param window  
       Current window  
  
@param appId  
       Application ID to be registered  
  

### unregisterTargetForPeerReady(window, appId) ###
  
Unregister the given application id with Chrome process  
  
@param window  
       Current window  
  
@param appId  
       Application ID to be registered  
  

### checkP2PRegistration(window, appId) ###
  
Checks if the given application's id is a registered peer target (with the Chrome process)  
  
@param window  
       Current window  
  
@param appId  
       Application ID to be updated with Chrome process  
  
Returns DOMRequest, if appId is registered then 'onsuccess' is called else 'onerror'  
  

### notifyUserAcceptedP2P(window, appId) ###
  
Notify the Chrome process that user has accepted to share nfc message on P2P UI  
  
@param window  
       Current window  
  
@param appId  
       Application ID that is capable of handling NFC_EVENT_PEER_READY event  
  

### notifySendFileStatus(window, status, requestId) ###
  
Notify the status of sendFile operation to Chrome process  
  
@param window  
       Current window  
  
@param status  
       Status of sendFile operation  
  
@param requestId  
       Request ID of SendFile DOM Request  
  

### startPoll(window) ###
  
Power on the NFC hardware and start polling for NFC tags or devices.  
  

### stopPoll(window) ###
  
Stop polling for NFC tags or devices. i.e. enter low power mode.  
  

### powerOff(window) ###
  
Power off the NFC hardware.  
  

## Constants ##

### NFC_EVENT_PEER_READY ###

### NFC_EVENT_PEER_LOST ###
