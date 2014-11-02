---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/gonk/nsIGonkMobileConnectionService.idl">Source file</a>
</div>
# nsIGonkMobileConnectionService #

## Methods ##

### notifyNetworkInfoChanged(clientId, networkInfo) ###

### notifyVoiceInfoChanged(clientId, voiceInfo) ###

### notifyDataInfoChanged(clientId, dataInfo) ###

### notifyDataError(clientId, message) ###

### notifySignalStrengthChanged(clientId, signal) ###

### notifyOperatorChanged(clientId, info) ###

### notifyOtaStatusChanged(clientId, status) ###

### notifyRadioStateChanged(clientId, radioState) ###

### notifyUssdReceived(clientId, message, sessionEnded) ###

### notifyEmergencyCallbackModeChanged(clientId, active, timeoutMs) ###

### notifyIccChanged(clientId, iccId) ###

### notifyNetworkSelectModeChanged(clientId, mode) ###

### notifySpnAvailable(clientId) ###

### notifyLastHomeNetworkChanged(clientId, network) ###

### notifyCFStateChanged(clientId, action, reason, number, timeSeconds, serviceClass) ###

### notifyCdmaInfoRecDisplay(clientId, display) ###
  
Notify Display Info from received Cdma-Info-Record.  
See 3.7.4.1 Display in 3GPP2 C.S0005-F.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param display  
The string to be displayed.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>display</td>
<td>The string to be displayed.  
</td>
</tr>

</table>

### notifyCdmaInfoRecCalledPartyNumber(clientId, type, plan, number, pi, si) ###
  
Notify Called Party Number from received Cdma-Info-Record.  
See 3.7.4.2 Called Party Number in 3GPP2 C.S0005-F.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param type  
       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
@param plan  
       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
@param number  
       The string presentation of the number.  
@param pi (2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
@param si (2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>type</td>
<td>       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>plan</td>
<td>       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>number</td>
<td>       The string presentation of the number.  
</td>
</tr>

<tr>
<td>pi</td>
<td>(2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>si</td>
<td>(2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

</table>

### notifyCdmaInfoRecCallingPartyNumber(clientId, type, plan, number, pi, si) ###
  
Notify Calling Party Number from received Cdma-Info-Record.  
See 3.7.4.3 Calling Party Number in 3GPP2 C.S0005-F.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param type  
       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
@param plan  
       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
@param number  
       The string presentation of the number.  
@param pi (2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
@param si (2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>type</td>
<td>       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>plan</td>
<td>       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>number</td>
<td>       The string presentation of the number.  
</td>
</tr>

<tr>
<td>pi</td>
<td>(2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>si</td>
<td>(2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

</table>

### notifyCdmaInfoRecConnectedPartyNumber(clientId, type, plan, number, pi, si) ###
  
Notify Connected Party Number from received Cdma-Info-Record.  
See 3.7.4.4 Connected Party Number in 3GPP2 C.S0005-F.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param type  
       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
@param plan  
       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
@param number  
       The string presentation of the number.  
@param pi (2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
@param si (2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>type</td>
<td>       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>plan</td>
<td>       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>number</td>
<td>       The string presentation of the number.  
</td>
</tr>

<tr>
<td>pi</td>
<td>(2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>si</td>
<td>(2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

</table>

### notifyCdmaInfoRecSignal(clientId, type, alertPitch, signal) ###
  
Notify Signal Info from received Cdma-Info-Record.  
See 3.7.4.5 Signal in 3GPP2 C.S0005-F.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param type  
       The signal type. (2-bit binary)  
       See Table 3.7.5.5-1 in 3GPP2 C.S0005-F.  
@param alertPitch  
       The pitch of the alerting signal. (2-bit binary)  
       See Table 3.7.5.5-2 in 3GPP2 C.S0005-F.  
@param signal  
       The signal code. (6-bit binary)  
       See Table 3.7.5.5-3, 3.7.5.5-4, 3.7.5.5-5 in 3GPP2 C.S0005-F.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>type</td>
<td>       The signal type. (2-bit binary)  
       See Table 3.7.5.5-1 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>alertPitch</td>
<td>       The pitch of the alerting signal. (2-bit binary)  
       See Table 3.7.5.5-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>signal</td>
<td>       The signal code. (6-bit binary)  
       See Table 3.7.5.5-3, 3.7.5.5-4, 3.7.5.5-5 in 3GPP2 C.S0005-F.  
</td>
</tr>

</table>

### notifyCdmaInfoRecRedirectingNumber(clientId, type, plan, number, pi, si, reason) ###
  
Notify Redirecting Number from received Cdma-Info-Record.  
See 3.7.4.11 Redirecting Number in 3GPP2 C.S0005-F.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param type  
       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
@param plan  
       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
@param number  
       The string presentation of the number.  
@param pi (2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
@param si (2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
@param reason (4-bit binary)  
       The redirection reason.  
       See Table 3.7.5.11-1 in 3GPP2 C.S0005-F.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>type</td>
<td>       The type of number. (3-bit binary)  
       See Table 2.7.1.3.2.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>plan</td>
<td>       The numbering plan. (4-bit binary)  
       See Table 2.7.1.3.2.4-3 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>number</td>
<td>       The string presentation of the number.  
</td>
</tr>

<tr>
<td>pi</td>
<td>(2-bit binary)  
       The Presentation indicator of the number.  
       See Table 2.7.4.4-1 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>si</td>
<td>(2-bit binary)  
       The Screening Indicator of the number.  
       See Table 2.7.4.4-2 in 3GPP2 C.S0005-F.  
</td>
</tr>

<tr>
<td>reason</td>
<td>(4-bit binary)  
       The redirection reason.  
       See Table 3.7.5.11-1 in 3GPP2 C.S0005-F.  
</td>
</tr>

</table>

### notifyCdmaInfoRecLineControl(clientId, polarityIncluded, toggle, reverse, powerDenial) ###
  
Notify Line Control from received Cdma-Info-Record.  
See 3.7.4.15 Line Control in 3GPP2 C.S0005-F.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param polarityIncluded (1-bit)  
       Polarity parameter included.  
@param toggle (1-bit)  
       Toggle mode.  
@param reverse (1-bit)  
       Reverse polarity.  
@param powerDenial (8-bit)  
       Power denial timeout.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>polarityIncluded</td>
<td>(1-bit)  
       Polarity parameter included.  
</td>
</tr>

<tr>
<td>toggle</td>
<td>(1-bit)  
       Toggle mode.  
</td>
</tr>

<tr>
<td>reverse</td>
<td>(1-bit)  
       Reverse polarity.  
</td>
</tr>

<tr>
<td>powerDenial</td>
<td>(8-bit)  
       Power denial timeout.  
</td>
</tr>

</table>

### notifyCdmaInfoRecClir(clientId, cause) ###
  
Notify CLIR from received Cdma-Info-Record.  
See 'ANNEX 1 Country-Specific Record Type for Japan' in T53.  
http://www.arib.or.jp/english/html/overview/doc/T53v6_5_pdf/5_ANNEX_v6_5.pdf  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param cause  
       Reason code. (8-bit binary)  
       See Table A 1.1-1 in T53.  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>cause</td>
<td>       Reason code. (8-bit binary)  
       See Table A 1.1-1 in T53.  
</td>
</tr>

</table>

### notifyCdmaInfoRecAudioControl(clientId, upLink, downLink) ###
  
Notify Audio Control from received Cdma-Info-Record.  
  
Note: No information from ARIB about Audio Control.  
      It seems obsolete according to ANNEX 1 in T53.  
      upLink/downLink are 'byte' value according to ril.h.  
      Treat them as 'signed short' to preserve the flexibility when needed.  
  
@param clientId  
       The ID of radioInterface where this info is notified from.  
@param upLink  
@param downLink  
  

#### Parameters ####

<table>

<tr>
<td>clientId</td>
<td>       The ID of radioInterface where this info is notified from.  
</td>
</tr>

<tr>
<td>upLink</td>
<td></td>
</tr>

<tr>
<td>downLink</td>
<td></td>
</tr>

</table>
