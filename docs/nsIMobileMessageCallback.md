---
layout: default
---

# nsIMobileMessageCallback #

## Methods ##

### notifyMessageSent ###

|message| can be nsIDOMMoz{Mms,Sms}Message.


### notifySendMessageFailed ###

### notifyMessageGot ###

|message| can be nsIDOMMoz{Mms,Sms}Message.


### notifyGetMessageFailed ###

### notifyMessageDeleted ###

### notifyDeleteMessageFailed ###

### notifyMessageMarkedRead ###

### notifyMarkMessageReadFailed ###

### notifySegmentInfoForTextGot ###

### notifyGetSegmentInfoForTextFailed ###

### notifyGetSmscAddress ###

 SMSC Address get/set result


### notifyGetSmscAddressFailed ###

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
