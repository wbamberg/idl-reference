---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/icc/interfaces/nsIIccProvider.idl">Source file</a>
</div>

# nsIIccProvider #
<pre>  
XPCOM component (in the content process) that provides the ICC information.  
  
</pre>
## Methods ##

### registerIccMsg(clientId, listener) ###
<pre>  
Called when a content process registers receiving unsolicited messages from  
RadioInterfaceLayer in the chrome process. Only a content process that has  
the 'mobileconnection' permission is allowed to register.  
  
</pre>
### unregisterIccMsg(clientId, listener) ###

### getIccInfo(clientId) ###
<pre>  
UICC Information  
  
</pre>
### getCardState(clientId) ###
<pre>  
Card State  
  
One of the nsIIccProvider.CARD_STATE_* values.  
  
</pre>
### sendStkResponse(clientId, window, command, response) ###
<pre>  
STK interfaces.  
  
</pre>
### sendStkMenuSelection(clientId, window, itemIdentifier, helpRequested) ###

### sendStkTimerExpiration(clientId, window, timer) ###

### sendStkEventDownload(clientId, window, event) ###

### getCardLockState(clientId, window, lockType) ###
<pre>  
Card lock interfaces.  
  
</pre>
### unlockCardLock(clientId, window, info) ###

### setCardLock(clientId, window, info) ###

### getCardLockRetryCount(clientId, window, lockType) ###

### readContacts(clientId, window, contactType) ###
<pre>  
Phonebook interfaces.  
  
</pre>
### updateContact(clientId, window, contactType, contact, pin2) ###

### iccOpenChannel(clientId, window, aid) ###
<pre>  
Secure Card Icc communication channel  
  
</pre>
### iccExchangeAPDU(clientId, window, channel, apdu) ###

### iccCloseChannel(clientId, window, channel) ###

### matchMvno(clientId, window, mvnoType, mvnoData) ###
<pre>  
Helpers  
  
</pre>
## Constants ##

### CARD_STATE_UNKNOWN ###

### CARD_STATE_READY ###

### CARD_STATE_PIN_REQUIRED ###

### CARD_STATE_PUK_REQUIRED ###

### CARD_STATE_PERMANENT_BLOCKED ###

### CARD_STATE_PERSONALIZATION_IN_PROGRESS ###

### CARD_STATE_PERSONALIZATION_READY ###

### CARD_STATE_NETWORK_LOCKED ###

### CARD_STATE_NETWORK_SUBSET_LOCKED ###

### CARD_STATE_CORPORATE_LOCKED ###

### CARD_STATE_SERVICE_PROVIDER_LOCKED ###

### CARD_STATE_SIM_LOCKED ###

### CARD_STATE_NETWORK_PUK_REQUIRED ###

### CARD_STATE_NETWORK_SUBSET_PUK_REQUIRED ###

### CARD_STATE_CORPORATE_PUK_REQUIRED ###

### CARD_STATE_SERVICE_PROVIDER_PUK_REQUIRED ###

### CARD_STATE_SIM_PUK_REQUIRED ###

### CARD_STATE_NETWORK1_LOCKED ###

### CARD_STATE_NETWORK2_LOCKED ###

### CARD_STATE_HRPD_NETWORK_LOCKED ###

### CARD_STATE_RUIM_CORPORATE_LOCKED ###

### CARD_STATE_RUIM_SERVICE_PROVIDER_LOCKED ###

### CARD_STATE_RUIM_LOCKED ###

### CARD_STATE_NETWORK1_PUK_REQUIRED ###

### CARD_STATE_NETWORK2_PUK_REQUIRED ###

### CARD_STATE_HRPD_NETWORK_PUK_REQUIRED ###

### CARD_STATE_RUIM_CORPORATE_PUK_REQUIRED ###

### CARD_STATE_RUIM_SERVICE_PROVIDER_PUK_REQUIRED ###

### CARD_STATE_RUIM_PUK_REQUIRED ###

### CARD_STATE_ILLEGAL ###

### CARD_STATE_UNDETECTED ###
