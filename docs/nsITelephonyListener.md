---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/telephony/nsITelephonyService.idl">Source file</a>
</div>

# nsITelephonyListener #

## Methods ##

### callStateChanged(clientId, callIndex, callState, number, numberPresentation, name, namePresentation, isOutgoing, isEmergency, isConference, isSwitchable, isMergeable) ###
<pre>  
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
  
</pre>
#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>Indicate the RIL client, 0 ~ (number of client - 1).  
</td>
</tr>

<tr>
<td>callIndex</td>
<td>       Call identifier assigned by the RIL.  
</td>
</tr>

<tr>
<td>callState</td>
<td>       One of the nsITelephonyService::CALL_STATE_* values.  
</td>
</tr>

<tr>
<td>number</td>
<td>       Number of the other party.  
</td>
</tr>

<tr>
<td>numberPresentation</td>
<td>       Presentation of the call number.  
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.  
</td>
</tr>

<tr>
<td>name</td>
<td>       Name of the other party.  
</td>
</tr>

<tr>
<td>namePresentation</td>
<td>       Presentation of the call name.  
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.  
</td>
</tr>

<tr>
<td>isOutgoing</td>
<td>       Indicates whether this call is outgoing or incoming.  
</td>
</tr>

<tr>
<td>isEmergency</td>
<td>       Indicates whether this call is an emergency call.  
</td>
</tr>

<tr>
<td>isConference</td>
<td>       Indicates whether this call is a conference call.  
</td>
</tr>

<tr>
<td>isSwitchable</td>
<td>       Indicates whether this call can be switched between states of  
       nsITelephonyService::CALL_STATE_CONNECTED and  
       nsITelephonyService::CALL_STATE_HELD.  
</td>
</tr>

<tr>
<td>isMergeable</td>
<td>       Indicates whether this call be be added into a conference.  
</td>
</tr>

</table>

### conferenceCallStateChanged(callState) ###
<pre>  
Called when participants of a conference call have been updated, and the  
conference call state changes.  
  
@param callState  
       Possible values are: nsITelephonyService::CALL_STATE_UNKNOWN,  
       nsITelephonyService::CALL_STATE_HELD,  
       nsITelephonyService::CALL_STATE_CONNECTED.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>callState</td>
<td>       Possible values are: nsITelephonyService::CALL_STATE_UNKNOWN,  
       nsITelephonyService::CALL_STATE_HELD,  
       nsITelephonyService::CALL_STATE_CONNECTED.  
</td>
</tr>

</table>

### enumerateCallStateComplete() ###
<pre>  
Called when enumeration asked by nsITelephonyService::enumerateCalls  
is completed.  
  
</pre>
### enumerateCallState(clientId, callIndex, callState, number, numberPresentation, name, namePresentation, isOutgoing, isEmergency, isConference, isSwitchable, isMergeable) ###
<pre>  
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
  
</pre>
#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>Indicate the RIL client, 0 ~ (number of client - 1).  
</td>
</tr>

<tr>
<td>callIndex</td>
<td>       Call identifier assigned by the RIL.  
</td>
</tr>

<tr>
<td>callState</td>
<td>       One of the nsITelephonyService::CALL_STATE_* values.  
</td>
</tr>

<tr>
<td>number</td>
<td>       Number of the other party.  
</td>
</tr>

<tr>
<td>numberPresentation</td>
<td>       Presentation of the call number.  
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.  
</td>
</tr>

<tr>
<td>name</td>
<td>       Name of the other party.  
</td>
</tr>

<tr>
<td>namePresentation</td>
<td>       Presentation of the call name.  
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.  
</td>
</tr>

<tr>
<td>isOutgoing</td>
<td>       Indicates whether this call is outgoing or incoming.  
</td>
</tr>

<tr>
<td>isConference</td>
<td>       Indicates whether this call is a conference call.  
</td>
</tr>

<tr>
<td>isSwitchable</td>
<td>       Indicates whether this call can be switched between states of  
       nsITelephonyService::CALL_STATE_CONNECTED and  
       nsITelephonyService::CALL_STATE_HELD.  
</td>
</tr>

<tr>
<td>isMergeable</td>
<td>       Indicates whether this call be be added into a conference.  
</td>
</tr>

</table>

### supplementaryServiceNotification(clientId, callIndex, notification) ###
<pre>  
Notify when RIL receives supplementary service notification.  
  
@param clientId  
Indicate the RIL client, 0 ~ (number of client - 1).  
@param callIndex  
       Call identifier assigned by the RIL. -1 if not specified  
@param notification  
       One of the nsITelephonyService::NOTIFICATION_* values.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>Indicate the RIL client, 0 ~ (number of client - 1).  
</td>
</tr>

<tr>
<td>callIndex</td>
<td>       Call identifier assigned by the RIL. -1 if not specified  
</td>
</tr>

<tr>
<td>notification</td>
<td>       One of the nsITelephonyService::NOTIFICATION_* values.  
</td>
</tr>

</table>

### notifyError(clientId, callIndex, error) ###
<pre>  
Called when RIL error occurs.  
  
@param clientId  
Indicate the RIL client, 0 ~ (number of client - 1).  
@param callIndex  
       Call identifier assigned by the RIL. -1 if no connection  
@param error  
       Error from RIL.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>Indicate the RIL client, 0 ~ (number of client - 1).  
</td>
</tr>

<tr>
<td>callIndex</td>
<td>       Call identifier assigned by the RIL. -1 if no connection  
</td>
</tr>

<tr>
<td>error</td>
<td>       Error from RIL.  
</td>
</tr>

</table>

### notifyCdmaCallWaiting(clientId, number, numberPresentation, name, namePresentation) ###
<pre>  
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
  
</pre>
#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>Indicate the RIL client, 0 ~ (number of client - 1).  
</td>
</tr>

<tr>
<td>number</td>
<td>       Number of the other party.  
</td>
</tr>

<tr>
<td>numberPresentation</td>
<td>       Presentation of the call number.  
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.  
</td>
</tr>

<tr>
<td>name</td>
<td>       Name of the other party.  
</td>
</tr>

<tr>
<td>namePresentation</td>
<td>       Presentation of the call name.  
       One of the nsITelephonyProvider::CALL_PRESENTATION_* values.  
</td>
</tr>

</table>

### notifyConferenceError(name, message) ###
<pre>  
Called when RIL error occurs to creating or separating a conference call.  
  
@param name  
       Error name. Possible values are addError and removeError.  
@param message  
       Detailed error message from RIL.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       Error name. Possible values are addError and removeError.  
</td>
</tr>

<tr>
<td>message</td>
<td>       Detailed error message from RIL.  
</td>
</tr>

</table>
