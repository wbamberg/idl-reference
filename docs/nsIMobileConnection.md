---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsIMobileConnectionService.idl">Source file</a>
</div>

# nsIMobileConnection #

## Methods ##

### registerListener(listener) ###
  
Called when any one who is interested in receiving unsolicited messages  
from this nsIMobileConnection instance.  
  

### unregisterListener(listener) ###

### getSupportedNetworkTypes(types, length) ###
  
The network types supported by this radio.  
  
  

#### Returns ####

<table>

<tr>
<td>an array of DOMString  
        Possible values: 'gsm', 'wcdma', 'cdma', 'evdo', 'lte'.  
</td>
</tr>

</table>

### getNetworks(requestCallback) ###
  
Search for available networks.  
  
  
If successful, the notifyGetNetworksSuccess() will be called. And the  
result will be an array of nsIMobileNetworkInfo.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### selectNetwork(network, requestCallback) ###
  
Manually selects the passed in network, overriding the radio's current  
selection.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>network</td>
<td>       The manually selecting network.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### selectNetworkAutomatically(requestCallback) ###
  
Tell the radio to automatically select a network.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setPreferredNetworkType(type, requestCallback) ###
  
Set preferred network type.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>type</td>
<td>       DOMString indicates the desired preferred network type.  
       Possible values: 'wcdma/gsm', 'gsm', 'wcdma', 'wcdma/gsm-auto',  
       'cdma/evdo', 'cdma', 'evdo', 'wcdma/gsm/cdma/evdo',  
       'lte/cdma/evdo', 'lte/wcdma/gsm', 'lte/wcdma/gsm/cdma/evdo' or  
       'lte'.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getPreferredNetworkType(requestCallback) ###
  
Query current preferred network type.  
  
  
If successful, the notifySuccessString() will be called. And the result  
will be a string indicating the current preferred network type. The value  
will be either 'wcdma/gsm', 'gsm', 'wcdma', 'wcdma/gsm-auto', 'cdma/evdo',  
'cdma', 'evdo', 'wcdma/gsm/cdma/evdo', 'lte/cdma/evdo', 'lte/wcdma/gsm',  
'lte/wcdma/gsm/cdma/evdo' or 'lte'.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setRoamingPreference(mode, requestCallback) ###
  
Set roaming preference.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>mode</td>
<td>       DOMString indicates the desired roaming preference.  
       Possible values: 'home', 'affiliated', or 'any'.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getRoamingPreference(requestCallback) ###
  
Query current roaming preference.  
  
  
If successful, the notifySuccessWithString() will be called. And the result  
will be a string indicating the current roaming preference. The value will  
be either 'home', 'affiliated', or 'any'.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setVoicePrivacyMode(enabled, requestCallback) ###
  
Set voice privacy preference.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>enabled</td>
<td>       Boolean indicates the preferred voice privacy mode used in voice  
       scrambling in CDMA networks. 'True' means the enhanced voice security  
       is required.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getVoicePrivacyMode(requestCallback) ###
  
Query current voice privacy mode.  
  
  
If successful, the notifySuccessWithBoolean() will be called. And the result  
will be a boolean indicating the current voice privacy mode.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### sendMMI(mmi, requestCallback) ###
  
Send a MMI message.  
  
  
If successful, the notifySendCancelMmiSuccess*() will be called. And the  
result will contain the information about the mmi operation.  
  
Otherwise, the notifyError() will be called.  
  

#### Parameters ####

<table>

<tr>
<td>mmi</td>
<td>       DOMString containing an MMI string that can be associated to a  
       USSD request or other RIL functionality.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### cancelMMI(requestCallback) ###
  
Cancel the current MMI request if one exists.  
  
  
If successful, the notifySendCancelMmiSuccess*() will be called. And the  
result will contain the information about the mmi operation.  
  
Otherwise, the notifyError() will be called.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getCallForwarding(reason, requestCallback) ###
  
Queries current call forwarding options.  
  
  
If successful, the notifyGetCallForwardingSuccess() will be called. And the  
result will be an array of nsIMobileCallForwardingOptions.  
@see nsIMobileCallForwardingOptions for the detail of result.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>reason</td>
<td>       Indicates the reason the call is being forwarded. It shall be one of  
       the nsIMobileConnectionService.CALL_FORWARD_REASON_* values.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setCallForwarding(action, reason, number, timeSeconds, serviceClass, requestCallback) ###
  
Configures call forwarding options.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>action</td>
<td>       One of the nsIMobileConnection.CALL_FORWARD_ACTION_* values.  
</td>
</tr>

<tr>
<td>reason</td>
<td>       One of the nsIMobileConnection.CALL_FORWARD_REASON_* values.  
</td>
</tr>

<tr>
<td>number</td>
<td>       Phone number of forwarding address.  
</td>
</tr>

<tr>
<td>timeSeconds</td>
<td>       When "no reply" is enabled or queried, this gives the time in  
       seconds to wait before call is forwarded.  
</td>
</tr>

<tr>
<td>serviceClass</td>
<td>       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getCallBarring(program, password, serviceClass, requestCallback) ###
  
Queries current call barring status.  
  
  
If successful, the notifyGetCallBarringSuccess() will be called. And the  
result will contain correct 'enabled' property indicating the status of  
this rule.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>program</td>
<td>       One of the nsIMobileConnection.CALL_BARRING_PROGRAM_* values.  
</td>
</tr>

<tr>
<td>password</td>
<td>       Call barring password. Use "" if no password specified.  
</td>
</tr>

<tr>
<td>serviceClass</td>
<td>       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setCallBarring(program, enabled, password, serviceClass, requestCallback) ###
  
Configures call barring option.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>program</td>
<td>       One of the nsIMobileConnection.CALL_BARRING_PROGRAM_* values.  
</td>
</tr>

<tr>
<td>enabled</td>
<td>       Enable or disable the call barring program.  
</td>
</tr>

<tr>
<td>password</td>
<td>       Call barring password. Use "" if no password specified.  
</td>
</tr>

<tr>
<td>serviceClass</td>
<td>       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### changeCallBarringPassword(pin, newPin, requestCallback) ###
  
Change call barring facility password.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>pin</td>
<td>       Old call barring password.  
</td>
</tr>

<tr>
<td>newPin</td>
<td>       New call barring password.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setCallWaiting(enabled, requestCallback) ###
  
Configures call waiting options.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>enabled</td>
<td>       Boolean indicates the desired call waiting status.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getCallWaiting(requestCallback) ###
  
Queries current call waiting options.  
  
  
If successful, the notifySuccessWithBoolean() will be called. And the result  
will be a boolean indicating the call waiting status.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setCallingLineIdRestriction(clirMode, requestCallback) ###
  
Enables or disables the presentation of the calling line identity (CLI) to  
the called party when originating a call.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'InvalidParameter',  
'IllegalSIMorME', or 'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>clirMode</td>
<td>       One of the nsIMobileConnection.CLIR_* values.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getCallingLineIdRestriction(requestCallback) ###
  
Queries current CLIR status.  
  
  
If successful, the notifyGetClirStatusSuccess() will be called. And the  
result will be a an object containing CLIR 'n' and 'm' parameter.  
@see MozClirStatus for the detail of result.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### exitEmergencyCbMode(requestCallback) ###
  
Exit emergency callback mode.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'RadioNotAvailable', 'RequestNotSupported', 'IllegalSIMorME', or  
'GenericFailure'.  
  

#### Parameters ####

<table>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### setRadioEnabled(enabled, requestCallback) ###
  
Set radio enabled/disabled.  
  
  
If successful, the notifySuccess() will be called.  
  
Otherwise, the notifyError() will be called, and the error will be either  
'InvalidStateError', 'RadioNotAvailable', 'IllegalSIMorME', or  
'GenericFailure'.  
  
Note: Request is not available when radioState is null, 'enabling', or  
'disabling'. Calling the function in above conditions will receive  
'InvalidStateError' error.  
  

#### Parameters ####

<table>

<tr>
<td>enabled</td>
<td>       Boolean indicates the desired radio power. True to enable the radio.  
</td>
</tr>

<tr>
<td>requestCallback</td>
<td>       Called when request is finished.  
</td>
</tr>

</table>

### getNeighboringCellIds(callback) ###
  
Request neighboring cell ids in GSM/UMTS network.  
  
  

#### Parameters ####

<table>

<tr>
<td>callback</td>
<td>       Called when request is finished. See nsINeighboringCellIdsCallback  
       for details.  
</td>
</tr>

</table>

### getCellInfoList(callback) ###
  
Request all of the current cell information known to the radio, including  
neighboring cells.  
  
  

#### Parameters ####

<table>

<tr>
<td>callback</td>
<td>       Called when request is finished. See nsICellInfoListCallback  
       for details.  
</td>
</tr>

</table>

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
