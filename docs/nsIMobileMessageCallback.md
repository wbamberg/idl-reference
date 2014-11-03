---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobilemessage/interfaces/nsIMobileMessageCallback.idl">Source file</a>
</div>

# nsIMobileMessageCallback #

## Methods ##

### notifyMessageSent(message) ###
  
|message| can be nsIDOMMoz{Mms,Sms}Message.  
  

### notifySendMessageFailed(error, message) ###

### notifyMessageGot(message) ###
  
|message| can be nsIDOMMoz{Mms,Sms}Message.  
  

### notifyGetMessageFailed(error) ###

### notifyMessageDeleted(deleted, count) ###

### notifyDeleteMessageFailed(error) ###

### notifyMessageMarkedRead(read) ###

### notifyMarkMessageReadFailed(error) ###

### notifySegmentInfoForTextGot(segments, charsPerSegment, charsAvailableInLastSegment) ###

### notifyGetSegmentInfoForTextFailed(error) ###

### notifyGetSmscAddress(aSmscAddress) ###
  
 SMSC Address get/set result  
  

### notifyGetSmscAddressFailed(error) ###

## Constants ##

### SUCCESS_NO_ERROR ###
  
All SMS related errors.  
Make sure to keep this list in sync with the list in:  
embedding/android/GeckoSmsManager.java  
  

### NO_SIGNAL_ERROR ###

### NOT_FOUND_ERROR ###

### UNKNOWN_ERROR ###

### INTERNAL_ERROR ###

### NO_SIM_CARD_ERROR ###

### RADIO_DISABLED_ERROR ###

### INVALID_ADDRESS_ERROR ###

### FDN_CHECK_ERROR ###

### NON_ACTIVE_SIM_CARD_ERROR ###

### STORAGE_FULL_ERROR ###

### SIM_NOT_MATCHED_ERROR ###
