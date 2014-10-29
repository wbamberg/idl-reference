---
layout: default
---

# nsICellBroadcastService #

XPCOM component that provides the cell broadcast information.


## Methods ##

### registerListener ###

Called to register receiving cellbroadcast messages.

'cellbroadcast' permission is required for registration/unregistration.


### unregisterListener ###

## Constants ##

### GSM_GEOGRAPHICAL_SCOPE_CELL_IMMEDIATE ###

Constant definitions of predefined GSM Geographic Scope
See 3GPP TS 23.041 clause 9.4.1.2.1 Serial Number


### GSM_GEOGRAPHICAL_SCOPE_PLMN ###

### GSM_GEOGRAPHICAL_SCOPE_LOCATION_AREA ###

### GSM_GEOGRAPHICAL_SCOPE_CELL ###

### GSM_GEOGRAPHICAL_SCOPE_INVALID ###

### GSM_MESSAGE_CLASS_0 ###

Constant definitions of predefined GSM Message Class
See 3GPP TS 23.038 clause 5 CBS Data Coding Scheme


### GSM_MESSAGE_CLASS_1 ###

### GSM_MESSAGE_CLASS_2 ###

### GSM_MESSAGE_CLASS_3 ###

### GSM_MESSAGE_CLASS_USER_1 ###

### GSM_MESSAGE_CLASS_USER_2 ###

### GSM_MESSAGE_CLASS_NORMAL ###

### GSM_MESSAGE_CLASS_INVALID ###

### GSM_ETWS_WARNING_EARTHQUAKE ###

Constant definitions of predefined GSM ETWS Warning Types
see 3GPP TS 23.041 clause 9.3.24 Warning-Type


### GSM_ETWS_WARNING_TSUNAMI ###

### GSM_ETWS_WARNING_EARTHQUAKE_TSUNAMI ###

### GSM_ETWS_WARNING_TEST ###

### GSM_ETWS_WARNING_OTHER ###

### GSM_ETWS_WARNING_INVALID ###

### CDMA_SERVICE_CATEGORY_INVALID ###

Attribute CdmaServiceCategory is only valid in CDMA network.
Set to CDMA_SERVICE_CATEGORY_INVALID if received from GSM/UMTS network.

