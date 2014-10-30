---
layout: default
---

# nsIMobileConnection #

## Methods ##

### registerListener ###
  
Called when any one who is interested in receiving unsolicited messages  
from this nsIMobileConnection instance.  
  

### unregisterListener ###

### getSupportedNetworkTypes ###
  
The network types supported by this radio.  
  
@return an array of DOMString  
        Possible values: 'gsm', 'wcdma', 'cdma', 'evdo', 'lte'.  
  

### getNetworks ###
  
Search for available networks.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifyGetNetworksSuccess() will be called. And the  
result will be an array of nsIMobileNetworkInfo.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### selectNetwork ###
  
Manually selects the passed in network, overriding the radio's current  
selection.  
  
@param network  
       The manually selecting network.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### selectNetworkAutomatically ###
  
Tell the radio to automatically select a network.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### setPreferredNetworkType ###
  
Set preferred network type.  
  
@param type  
       DOMString indicates the desired preferred network type.  
       Possible values: 'wcdma/gsm', 'gsm', 'wcdma', 'wcdma/gsm-auto',  
       'cdma/evdo', 'cdma', 'evdo', 'wcdma/gsm/cdma/evdo',  
       'lte/cdma/evdo', 'lte/wcdma/gsm', 'lte/wcdma/gsm/cdma/evdo' or  
       'lte'.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### getPreferredNetworkType ###
  
Query current preferred network type.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccessString() will be called. And the result  
will be a string indicating the current preferred network type. The value  
will be either 'wcdma/gsm', 'gsm', 'wcdma', 'wcdma/gsm-auto', 'cdma/evdo',  
'cdma', 'evdo', 'wcdma/gsm/cdma/evdo', 'lte/cdma/evdo', 'lte/wcdma/gsm',  
'lte/wcdma/gsm/cdma/evdo' or 'lte'.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### setRoamingPreference ###
  
Set roaming preference.  
  
@param mode  
       DOMString indicates the desired roaming preference.  
       Possible values: 'home', 'affiliated', or 'any'.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### getRoamingPreference ###
  
Query current roaming preference.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccessWithString() will be called. And the result  
will be a string indicating the current roaming preference. The value will  
be either 'home', 'affiliated', or 'any'.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### setVoicePrivacyMode ###
  
Set voice privacy preference.  
  
@param enabled  
       Boolean indicates the preferred voice privacy mode used in voice  
       scrambling in CDMA networks. 'True' means the enhanced voice security  
       is required.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### getVoicePrivacyMode ###
  
Query current voice privacy mode.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccessWithBoolean() will be called. And the result  
will be a boolean indicating the current voice privacy mode.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### sendMMI ###
  
Send a MMI message.  
  
@param mmi  
       DOMString containing an MMI string that can be associated to a  
       USSD request or other RIL functionality.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySendCancelMmiSuccess*() will be called. And the  
result will contain the information about the mmi operation.  
  
Otherwise, the notifyError() will be called.  
  

### cancelMMI ###
  
Cancel the current MMI request if one exists.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySendCancelMmiSuccess*() will be called. And the  
result will contain the information about the mmi operation.  
  
Otherwise, the notifyError() will be called.  
  

### getCallForwarding ###
  
Queries current call forwarding options.  
  
@param reason  
       Indicates the reason the call is being forwarded. It shall be one of  
       the nsIMobileConnectionService.CALL_FORWARD_REASON_* values.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifyGetCallForwardingSuccess() will be called. And the  
result will be an array of nsIMobileCallForwardingOptions.  
@see nsIMobileCallForwardingOptions for the detail of result.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### setCallForwarding ###
  
Configures call forwarding options.  
  
@param action  
       One of the nsIMobileConnection.CALL_FORWARD_ACTION_* values.  
@param reason  
       One of the nsIMobileConnection.CALL_FORWARD_REASON_* values.  
@param number  
       Phone number of forwarding address.  
@param timeSeconds  
       When "no reply" is enabled or queried, this gives the time in  
       seconds to wait before call is forwarded.  
@param serviceClass  
       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### getCallBarring ###
  
Queries current call barring status.  
  
@param program  
       One of the nsIMobileConnection.CALL_BARRING_PROGRAM_* values.  
@param password  
       Call barring password. Use "" if no password specified.  
@param serviceClass  
       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifyGetCallBarringSuccess() will be called. And the  
result will contain correct 'enabled' property indicating the status of  
this rule.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### setCallBarring ###
  
Configures call barring option.  
  
@param program  
       One of the nsIMobileConnection.CALL_BARRING_PROGRAM_* values.  
@param enabled  
       Enable or disable the call barring program.  
@param password  
       Call barring password. Use "" if no password specified.  
@param serviceClass  
       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### changeCallBarringPassword ###
  
Change call barring facility password.  
  
@param pin  
       Old call barring password.  
@param newPin  
       New call barring password.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### setCallWaiting ###
  
Configures call waiting options.  
  
@param enabled  
       Boolean indicates the desired call waiting status.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### getCallWaiting ###
  
Queries current call waiting options.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccessWithBoolean() will be called. And the result  
will be a boolean indicating the call waiting status.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### setCallingLineIdRestriction ###
  
Enables or disables the presentation of the calling line identity (CLI) to  
the called party when originating a call.  
  
@param clirMode  
       One of the nsIMobileConnection.CLIR_* values.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

### getCallingLineIdRestriction ###
  
Queries current CLIR status.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifyGetClirStatusSuccess() will be called. And the  
result will be a an object containing CLIR 'n' and 'm' parameter.  
@see MozClirStatus for the detail of result.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### exitEmergencyCbMode ###
  
Exit emergency callback mode.  
  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

### setRadioEnabled ###
  
Set radio enabled/disabled.  
  
@param enabled  
       Boolean indicates the desired radio power. True to enable the radio.  
@param requestCallback  
       Called when request is finished.  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'InvalidStateError', 'RadioNotAvailable', 'IllegalSIMorME', or  
'GenericFailure'.  
  
Note: Request is not available when radioState is null, 'enabling', or  
'disabling'. Calling the function in above conditions will receive  
'InvalidStateError' error.  
  

### getNeighboringCellIds ###
  
Request neighboring cell ids in GSM/UMTS network.  
  
@param callback  
       Called when request is finished. See nsINeighboringCellIdsCallback  
       for details.  
  

### getCellInfoList ###
  
Request all of the current cell information known to the radio, including  
neighboring cells.  
  
@param callback  
       Called when request is finished. See nsICellInfoListCallback  
       for details.  
  

## Attributes ##

### serviceId ###

### lastKnownNetwork ###
  
String of format '<mcc>-<mnc>'. When changed, listener method  
'notifyLastKnownNetworkChanged' is called.  
  

### lastKnownHomeNetwork ###
  
String of format '<mcc>-<mnc>[-<spn>]'. When changed, listener method  
'notifyLastKnownHomeNetworkChanged' is called.  
  

### voice ###
  
Connection information about the voice.  
  

### data ###
  
Connection information about the data.  
  

### iccId ###
  
The integrated circuit card identifier of the SIM.  
  

### networkSelectionMode ###
  
The selection mode of the voice and data networks. One of the  
nsIMobileConnection.NETWORK_SELECTION_MODE_* values.  
  

### radioState ###
  
Current radio state. One of the nsIMobileConnection.MOBILE_RADIO_STATE_*  
values.  
  

## Constants ##

### ICC_SERVICE_CLASS_NONE ###

### ICC_SERVICE_CLASS_VOICE ###

### ICC_SERVICE_CLASS_DATA ###

### ICC_SERVICE_CLASS_FAX ###

### ICC_SERVICE_CLASS_SMS ###

### ICC_SERVICE_CLASS_DATA_SYNC ###

### ICC_SERVICE_CLASS_DATA_ASYNC ###

### ICC_SERVICE_CLASS_PACKET ###

### ICC_SERVICE_CLASS_PAD ###

### ICC_SERVICE_CLASS_MAX ###

### CALL_FORWARD_ACTION_UNKNOWN ###
  
Call forwarding action.  
  
@see 3GPP TS 27.007 7.11 "mode".  
  

### CALL_FORWARD_ACTION_DISABLE ###

### CALL_FORWARD_ACTION_ENABLE ###

### CALL_FORWARD_ACTION_QUERY_STATUS ###

### CALL_FORWARD_ACTION_REGISTRATION ###

### CALL_FORWARD_ACTION_ERASURE ###

### CALL_FORWARD_REASON_UNKNOWN ###
  
Call forwarding reason.  
  
@see 3GPP TS 27.007 7.11 "reason".  
  

### CALL_FORWARD_REASON_UNCONDITIONAL ###

### CALL_FORWARD_REASON_MOBILE_BUSY ###

### CALL_FORWARD_REASON_NO_REPLY ###

### CALL_FORWARD_REASON_NOT_REACHABLE ###

### CALL_FORWARD_REASON_ALL_CALL_FORWARDING ###

### CALL_FORWARD_REASON_ALL_CONDITIONAL_CALL_FORWARDING ###

### CALL_BARRING_PROGRAM_UNKNOWN ###
  
Call barring program.  
  

### CALL_BARRING_PROGRAM_ALL_OUTGOING ###

### CALL_BARRING_PROGRAM_OUTGOING_INTERNATIONAL ###

### CALL_BARRING_PROGRAM_OUTGOING_INTERNATIONAL_EXCEPT_HOME ###

### CALL_BARRING_PROGRAM_ALL_INCOMING ###

### CALL_BARRING_PROGRAM_INCOMING_ROAMING ###

### CLIR_DEFAULT ###
  
Calling line identification restriction constants.  
  
@see 3GPP TS 27.007 7.7 Defined values.  
  

### CLIR_INVOCATION ###

### CLIR_SUPPRESSION ###

### NETWORK_SELECTION_MODE_UNKNOWN ###
  
Network selection mode.  
  

### NETWORK_SELECTION_MODE_AUTOMATIC ###

### NETWORK_SELECTION_MODE_MANUAL ###

### MOBILE_RADIO_STATE_UNKNOWN ###
  
Mobile Radio State.  
  

### MOBILE_RADIO_STATE_ENABLING ###

### MOBILE_RADIO_STATE_ENABLED ###

### MOBILE_RADIO_STATE_DISABLING ###

### MOBILE_RADIO_STATE_DISABLED ###
