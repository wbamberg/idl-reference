---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/telephony/nsITelephonyService.idl">Source file</a>
</div>
# nsITelephonyService #
  
XPCOM component (in the content process) that provides the telephony  
information.  
  

## Methods ##

### registerListener(listener) ###
  
Called when a content process registers receiving unsolicited messages from  
RadioInterfaceLayer in the chrome process. Only a content process that has  
the 'telephony' permission is allowed to register.  
  

### unregisterListener(listener) ###

### enumerateCalls(listener) ###
  
Will continue calling listener.enumerateCallState until the listener  
returns false.  
  

### dial(clientId, number, isEmergency, callback) ###
  
Functionality for making and managing phone calls.  
  

### hangUp(clientId, callIndex) ###

### startTone(clientId, dtmfChar) ###

### stopTone(clientId) ###

### answerCall(clientId, callIndex) ###

### rejectCall(clientId, callIndex) ###

### holdCall(clientId, callIndex) ###

### resumeCall(clientId, callIndex) ###

### conferenceCall(clientId) ###

### separateCall(clientId, callIndex) ###

### hangUpConference(clientId, callback) ###

### holdConference(clientId) ###

### resumeConference(clientId) ###

### sendUSSD(clientId, ussd, callback) ###
  
Send an USSD on existing session. It results in error if the session is  
not existed.  
  
If successful, callback.notifySuccess() will be called.  
Otherwise, callback.notifyError() will be called.  
  

## Attributes ##

### defaultServiceId ###

### microphoneMuted ###

### speakerEnabled ###

## Constants ##

### CALL_STATE_UNKNOWN ###

### CALL_STATE_DIALING ###

### CALL_STATE_ALERTING ###

### CALL_STATE_CONNECTING ###

### CALL_STATE_CONNECTED ###

### CALL_STATE_HOLDING ###

### CALL_STATE_HELD ###

### CALL_STATE_RESUMING ###

### CALL_STATE_DISCONNECTING ###

### CALL_STATE_DISCONNECTED ###

### CALL_STATE_INCOMING ###

### NOTIFICATION_REMOTE_HELD ###

### NOTIFICATION_REMOTE_RESUMED ###

### CALL_PRESENTATION_ALLOWED ###

### CALL_PRESENTATION_RESTRICTED ###

### CALL_PRESENTATION_UNKNOWN ###

### CALL_PRESENTATION_PAYPHONE ###
