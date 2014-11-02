---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/voicemail/nsIVoicemailService.idl">Source file</a>
</div>

# nsIVoicemailProvider #

## Attributes ##

### serviceId ###

### number ###
  
Voicemail center number. When changed, |notifyInfoChanged| of registered  
nsIVoicemailListener instances are called.  
  
Default: null  
  
@see 3GPP TS 31.102 subclause 4.2.63 "EFmwis (Message Waiting Indication Status)"  
@see 3GPP TS 51.011 subclause 10.3.45 "EFmwis (Message Waiting Indication Status)"  
  

### displayName ###
  
Voicemail center display name. When changed, |notifyInfoChanged| of  
registered nsIVoicemailListener instances are called.  
  
Default: null  
  
@see 3GPP TS 31.102 subclause 4.2.63 "EFmwis (Message Waiting Indication Status)"  
@see 3GPP TS 51.011 subclause 10.3.45 "EFmwis (Message Waiting Indication Status)"  
  

### hasMessages ###
  
Whether or not there are messages waiting in the voicemail box. When  
changed, |notifyStatusChanged| of registered nsIVoicemailListener instances  
are called.  
  
Default: false  
  
@see 3GPP TS 23.038 chapter 4 "SMS Data Coding Scheme"  
@see 3GPP TS 23.040 subclause 9.2.3.24.2 "Special SMS Message Indication"  
  

### messageCount ###
  
When #hasMessages is true, #messageCount should be a positive number for  
the messages waiting, or -1 if the exact number is not available. When  
changed, |notifyStatusChanged| of registered nsIVoicemailListener instances  
are called.  
  
Default: 0  
  
@see 3GPP TS 23.040 subclause 9.2.3.24.2 "Special SMS Message Indication"  
  

### returnNumber ###
  
A Return Call Message indicates to the MS to inform the user that a call  
(e.g. a telephone call) can be established to the address specified within  
the #returnNumber. The #returnMessage (if present) gives displayable  
information (e.g. the number of waiting voice messages).  
  
When #hasMessages is true this may contain a non-null string as the phone  
number of a Return Call Message. When changed, |notifyStatusChanged| of  
registered nsIVoicemailListener instances are called.  
  
Default: null  
  
@see 3GPP TS 23.040 subclause 9.2.3.9 "TPProtocolIdentifier (TPPID)"  
  

### returnMessage ###
  
When #hasMessages is true this may contain a non-null string as the  
notification message of a Return Call Message. When changed,  
|notifyStatusChanged| of registered nsIVoicemailListener instances are  
called.  
  
Default: null  
  
@see 3GPP TS 23.040 subclause 9.2.3.9 "TPProtocolIdentifier (TPPID)"  
  
