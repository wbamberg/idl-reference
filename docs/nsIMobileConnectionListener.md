---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsIMobileConnectionService.idl">Source file</a>
</div>

# nsIMobileConnectionListener #

## Methods ##

### notifyVoiceChanged() ###
  
Notify when voice info is changed.  
  

### notifyDataChanged() ###
  
Notify when data info is changed.  
  

### notifyUssdReceived(message, sessionEnded) ###
  
Notify when ussd is received.  
  
  

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
  
Notify when data call is failed to establish.  
  
  

#### Parameters ####

<table>

<tr>
<td>message</td>
<td>       Error message from RIL.  
</td>
</tr>

</table>

### notifyCFStateChanged(action, reason, number, timeSeconds, serviceClass) ###
  
Notify when call forwarding state is changed.  
  
  

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
  
Notify when emergency callback mode is changed.  
  
  

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
  
Notify when ota status is changed.  
  
  

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
  
Notify when icc id is changed.  
  

### notifyRadioStateChanged() ###
  
Notify when radio state is changed.  
  

### notifyClirModeChanged(mode) ###
  
Notify when clir mode is changed.  
  
  

#### Parameters ####

<table>

<tr>
<td>mode</td>
<td>       One of the nsIMobileConnection.CLIR_* values.  
</td>
</tr>

</table>

### notifyLastKnownNetworkChanged() ###
  
Notify when last known network is changed.  
  

### notifyLastKnownHomeNetworkChanged() ###
  
Notify when last known home network is changed.  
  

### notifyNetworkSelectionModeChanged() ###
  
Notify when network selection mode is changed.  
  
