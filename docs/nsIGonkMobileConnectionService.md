---
layout: default
---

# nsIGonkMobileConnectionService #

## Methods ##

### notifyNetworkInfoChanged ###

### notifyVoiceInfoChanged ###

### notifyDataInfoChanged ###

### notifyDataError ###

### notifySignalStrengthChanged ###

### notifyOperatorChanged ###

### notifyOtaStatusChanged ###

### notifyRadioStateChanged ###

### notifyUssdReceived ###

### notifyEmergencyCallbackModeChanged ###

### notifyIccChanged ###

### notifyNetworkSelectModeChanged ###

### notifySpnAvailable ###

### notifyLastHomeNetworkChanged ###

### notifyCFStateChanged ###

### notifyCdmaInfoRecDisplay ###

Notify Display Info from received Cdma-Info-Record.
See 3.7.4.1 Display in 3GPP2 C.S0005-F.

@param clientId
       The ID of radioInterface where this info is notified from.
@param display
The string to be displayed.


### notifyCdmaInfoRecCalledPartyNumber ###

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


### notifyCdmaInfoRecCallingPartyNumber ###

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


### notifyCdmaInfoRecConnectedPartyNumber ###

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


### notifyCdmaInfoRecSignal ###

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


### notifyCdmaInfoRecRedirectingNumber ###

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


### notifyCdmaInfoRecLineControl ###

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


### notifyCdmaInfoRecClir ###

Notify CLIR from received Cdma-Info-Record.
See 'ANNEX 1 Country-Specific Record Type for Japan' in T53.
http://www.arib.or.jp/english/html/overview/doc/T53v6_5_pdf/5_ANNEX_v6_5.pdf

@param clientId
       The ID of radioInterface where this info is notified from.
@param cause
       Reason code. (8-bit binary)
       See Table A 1.1-1 in T53.


### notifyCdmaInfoRecAudioControl ###

Notify Audio Control from received Cdma-Info-Record.

Note: No information from ARIB about Audio Control.
      It seems obsolete according to ANNEX 1 in T53.
      upLink/downLink are 'byte' value according to ril.h.
      Treat them as 'signed short' to preserve the flexibility when needed.

@param clientId
       The ID of radioInterface where this info is notified from.
@param upLink
@param downLink

