---
layout: default
---

# nsIMobileConnectionCallback #

## Methods ##

### notifySuccess() ###
  
notify*Success*() will be called, when request is succeed.  
  

### notifySuccessWithString(result) ###

### notifySuccessWithBoolean(result) ###

### notifyGetNetworksSuccess(count, networks) ###

### notifySendCancelMmiSuccess(aServiceCode, aStatusMessage) ###

### notifySendCancelMmiSuccessWithInteger(aServiceCode, aStatusMessage, aAdditionalInformation) ###

### notifySendCancelMmiSuccessWithStrings(aServiceCode, aStatusMessage, aLength, aAdditionalInformation) ###

### notifySendCancelMmiSuccessWithCallForwardingOptions(aServiceCode, aStatusMessage, aLength, aAdditionalInformation) ###

### notifyGetCallForwardingSuccess(count, results) ###

### notifyGetCallBarringSuccess(program, enabled, serviceClass) ###

### notifyGetClirStatusSuccess(n, m) ###

### notifyError(name, message, serviceCode, additionalInformation) ###
  
notifyError() will be called, when request is failed.  
  
