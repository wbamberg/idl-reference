---
layout: default
---

# nsITelephonyListener #

## callStateChanged ##

Notified when a telephony call changes state.

@param clientId
Indicate the RIL client, 0 ~ (number of client - 1).
@param callIndex
       Call identifier assigned by the RIL.
@param callState
       One of the nsITelephonyService::CALL_STATE_* values.
@param number
       Number of the other party.
@param numberPresentation
       Presentation of the call number.
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.
@param name
       Name of the other party.
@param namePresentation
       Presentation of the call name.
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.
@param isOutgoing
       Indicates whether this call is outgoing or incoming.
@param isEmergency
       Indicates whether this call is an emergency call.
@param isConference
       Indicates whether this call is a conference call.
@param isSwitchable
       Indicates whether this call can be switched between states of
       nsITelephonyService::CALL_STATE_CONNECTED and
       nsITelephonyService::CALL_STATE_HELD.
@param isMergeable
       Indicates whether this call be be added into a conference.


## conferenceCallStateChanged ##

Called when participants of a conference call have been updated, and the
conference call state changes.

@param callState
       Possible values are: nsITelephonyService::CALL_STATE_UNKNOWN,
       nsITelephonyService::CALL_STATE_HELD,
       nsITelephonyService::CALL_STATE_CONNECTED.


## enumerateCallStateComplete ##

Called when enumeration asked by nsITelephonyService::enumerateCalls
is completed.


## enumerateCallState ##

Called when nsITelephonyService is asked to enumerate the current
telephony call state (nsITelephonyService::enumerateCalls). This is
called once per call that is currently managed by the RIL.

@param clientId
Indicate the RIL client, 0 ~ (number of client - 1).
@param callIndex
       Call identifier assigned by the RIL.
@param callState
       One of the nsITelephonyService::CALL_STATE_* values.
@param number
       Number of the other party.
@param numberPresentation
       Presentation of the call number.
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.
@param name
       Name of the other party.
@param namePresentation
       Presentation of the call name.
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.
@param isOutgoing
       Indicates whether this call is outgoing or incoming.
@param isConference
       Indicates whether this call is a conference call.
@param isSwitchable
       Indicates whether this call can be switched between states of
       nsITelephonyService::CALL_STATE_CONNECTED and
       nsITelephonyService::CALL_STATE_HELD.
@param isMergeable
       Indicates whether this call be be added into a conference.


## supplementaryServiceNotification ##

Notify when RIL receives supplementary service notification.

@param clientId
Indicate the RIL client, 0 ~ (number of client - 1).
@param callIndex
       Call identifier assigned by the RIL. -1 if not specified
@param notification
       One of the nsITelephonyService::NOTIFICATION_* values.


## notifyError ##

Called when RIL error occurs.

@param clientId
Indicate the RIL client, 0 ~ (number of client - 1).
@param callIndex
       Call identifier assigned by the RIL. -1 if no connection
@param error
       Error from RIL.


## notifyCdmaCallWaiting ##

Called when a waiting call comes in CDMA networks.

@param clientId
Indicate the RIL client, 0 ~ (number of client - 1).
@param number
       Number of the other party.
@param numberPresentation
       Presentation of the call number.
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.
@param name
       Name of the other party.
@param namePresentation
       Presentation of the call name.
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.


## notifyConferenceError ##

Called when RIL error occurs to creating or separating a conference call.

@param name
       Error name. Possible values are addError and removeError.
@param message
       Detailed error message from RIL.

