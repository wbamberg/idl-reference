---
layout: default
---

# nsIIccProvider #

XPCOM component (in the content process) that provides the ICC information.


## Methods ##

### registerIccMsg ###

Called when a content process registers receiving unsolicited messages from
RadioInterfaceLayer in the chrome process. Only a content process that has
the 'mobileconnection' permission is allowed to register.


### unregisterIccMsg ###

### getIccInfo ###

UICC Information


### getCardState ###

Card State

One of the nsIIccProvider.CARD_STATE_* values.


### sendStkResponse ###

STK interfaces.


### sendStkMenuSelection ###

### sendStkTimerExpiration ###

### sendStkEventDownload ###

### getCardLockState ###

Card lock interfaces.


### unlockCardLock ###

### setCardLock ###

### getCardLockRetryCount ###

### readContacts ###

Phonebook interfaces.


### updateContact ###

### iccOpenChannel ###

Secure Card Icc communication channel


### iccExchangeAPDU ###

### iccCloseChannel ###

### matchMvno ###

Helpers


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
