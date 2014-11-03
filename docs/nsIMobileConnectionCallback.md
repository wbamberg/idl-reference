---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsIMobileConnectionService.idl">Source file</a>
</div>

# nsIMobileConnectionCallback #

## Methods ##

### notifySuccess() ###
<code>  
notify*Success*() will be called, when request is succeed.  
  
</code>
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
<code>  
notifyError() will be called, when request is failed.  
  
</code>