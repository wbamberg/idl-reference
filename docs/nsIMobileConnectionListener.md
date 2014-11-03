---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsIMobileConnectionService.idl">Source file</a>
</div>

# nsIMobileConnectionListener #

## Methods ##

### notifyVoiceChanged() ###
<code>  
Notify when voice info is changed.  
  
</code>
### notifyDataChanged() ###
<code>  
Notify when data info is changed.  
  
</code>
### notifyUssdReceived(message, sessionEnded) ###
<code>  
Notify when ussd is received.  
  
@param message  
       The ussd request in string format.  
@param sessionEnded  
       Indicates whether the session is ended.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>message</td>
<td>       The ussd request in string format.  
</td>
</tr>

<tr>
<td>sessionEnded</td>
<td>       Indicates whether the session is ended.  
</td>
</tr>

</table>

### notifyDataError(message) ###
<code>  
Notify when data call is failed to establish.  
  
@param message  
       Error message from RIL.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>message</td>
<td>       Error message from RIL.  
</td>
</tr>

</table>

### notifyCFStateChanged(action, reason, number, timeSeconds, serviceClass) ###
<code>  
Notify when call forwarding state is changed.  
  
@param action  
       One of the nsIMobileConnection.CALL_FORWARD_ACTION_* values.  
@param reason  
       One of the nsIMobileConnection.CALL_FORWARD_REASON_* values.  
@param number  
       Phone number of forwarding address.  
@param timeSeconds  
       The time in seconds should wait before call is forwarded.  
@param serviceClass  
       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
  
</code>
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
<td>       The time in seconds should wait before call is forwarded.  
</td>
</tr>

<tr>
<td>serviceClass</td>
<td>       One of the nsIMobileConnection.ICC_SERVICE_CLASS_* values.  
</td>
</tr>

</table>

### notifyEmergencyCbModeChanged(active, timeoutMs) ###
<code>  
Notify when emergency callback mode is changed.  
  
@param active  
       Indicates whether the emergency callback mode is activated.  
@param timeoutMs  
       The timeout in millisecond for emergency callback mode.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>active</td>
<td>       Indicates whether the emergency callback mode is activated.  
</td>
</tr>

<tr>
<td>timeoutMs</td>
<td>       The timeout in millisecond for emergency callback mode.  
</td>
</tr>

</table>

### notifyOtaStatusChanged(status) ###
<code>  
Notify when ota status is changed.  
  
@param status  
       Ota status. Possible values: 'spl_unlocked', 'spc_retries_exceeded',  
       'a_key_exchanged', 'ssd_updated', 'nam_downloaded', 'mdn_downloaded',  
       'imsi_downloaded', 'prl_downloaded', 'committed', 'otapa_started',  
       'otapa_stopped', 'otapa_aborted'.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>status</td>
<td>       Ota status. Possible values: 'spl_unlocked', 'spc_retries_exceeded',  
       'a_key_exchanged', 'ssd_updated', 'nam_downloaded', 'mdn_downloaded',  
       'imsi_downloaded', 'prl_downloaded', 'committed', 'otapa_started',  
       'otapa_stopped', 'otapa_aborted'.  
</td>
</tr>

</table>

### notifyIccChanged() ###
<code>  
Notify when icc id is changed.  
  
</code>
### notifyRadioStateChanged() ###
<code>  
Notify when radio state is changed.  
  
</code>
### notifyClirModeChanged(mode) ###
<code>  
Notify when clir mode is changed.  
  
@param mode  
       One of the nsIMobileConnection.CLIR_* values.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>mode</td>
<td>       One of the nsIMobileConnection.CLIR_* values.  
</td>
</tr>

</table>

### notifyLastKnownNetworkChanged() ###
<code>  
Notify when last known network is changed.  
  
</code>
### notifyLastKnownHomeNetworkChanged() ###
<code>  
Notify when last known home network is changed.  
  
</code>
### notifyNetworkSelectionModeChanged() ###
<code>  
Notify when network selection mode is changed.  
  
</code>