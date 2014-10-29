---
layout: default
---

# nsIMobileConnectionListener #

## Methods ##

### notifyVoiceChanged ###

Notify when voice info is changed.


### notifyDataChanged ###

Notify when data info is changed.


### notifyUssdReceived ###

Notify when ussd is received.

@param message
       The ussd request in string format.
@param sessionEnded
       Indicates whether the session is ended.


### notifyDataError ###

Notify when data call is failed to establish.

@param message
       Error message from RIL.


### notifyCFStateChanged ###

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


### notifyEmergencyCbModeChanged ###

Notify when emergency callback mode is changed.

@param active
       Indicates whether the emergency callback mode is activated.
@param timeoutMs
       The timeout in millisecond for emergency callback mode.


### notifyOtaStatusChanged ###

Notify when ota status is changed.

@param status
       Ota status. Possible values: 'spl_unlocked', 'spc_retries_exceeded',
       'a_key_exchanged', 'ssd_updated', 'nam_downloaded', 'mdn_downloaded',
       'imsi_downloaded', 'prl_downloaded', 'committed', 'otapa_started',
       'otapa_stopped', 'otapa_aborted'.


### notifyIccChanged ###

Notify when icc id is changed.


### notifyRadioStateChanged ###

Notify when radio state is changed.


### notifyClirModeChanged ###

Notify when clir mode is changed.

@param mode
       One of the nsIMobileConnection.CLIR_* values.


### notifyLastKnownNetworkChanged ###

Notify when last known network is changed.


### notifyLastKnownHomeNetworkChanged ###

Notify when last known home network is changed.


### notifyNetworkSelectionModeChanged ###

Notify when network selection mode is changed.

