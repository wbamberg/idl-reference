---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/services/mobileid/interfaces/nsIMobileIdentityUIGlue.idl">Source file</a>
</div>

# nsIMobileIdentityUIGlue #

## Methods ##

### startFlow(manifestURL, iccInfo) ###
<code>  
Request the creation of a Mobile ID UI flow.  
  
The permission prompt starts the verification flow asking the user  
for permission to share her phone number and allowing her to choose  
an already known phone number, a SIM which phone number is unknown  
(even in a multi-SIM scenario) or an external phone number.  
Selecting a phone number implies giving permission to share it with the  
API caller, so the UI should be clear about this.  
  
@manifestURL manifest URL of the mobile ID requester.  
@iccInfo array of objects containing the information about the  
         SIM cards available in the device and that can be used for the  
         phone number verification and share process.  
  
Returns a Promise. An instance of nsIMobileIdentityUIGluePromptResult will  
be returned as result of the Promise or a single string containing an error  
in case of rejection.  
  
</code>
### verificationCodePrompt(retries, timeout, timeLeft) ###
<code>  
Will prompt the user to enter a code used to verify a phone number.  
This will only be called if an external phone number is selected in  
startFlow().  
  
@retries number of retries left to validate a verification code.  
@timeout the verification code expires after the timeout fires. This is  
         the total life time of the verification code.  
@timeLeft we might call verificationCodePrompt more than once for the  
          same verification flow (i.e. when the verification code entered  
          by the user is incorrect) so we give to the UI the amount of  
          time left before the verification code expires.  
  
Returns a Promise. The value of the resolved promise will be the  
verification code introduced through the UI or an error in case of  
rejection of the promise.  
  
</code>
### verify() ###
<code>  
Notify the UI about the start of the verification process.  
  
</code>
### error(error) ###
<code>  
Notify the UI about an error in the verification process.  
  
</code>
### verified(verifiedPhoneNumber) ###
<code>  
Notify the UI about the succesful phone number verification.  
  
</code>
## Attributes ##

### oncancel ###
  
Callback to be called when the user cancels the verification flow via UI.  
  

### onresendcode ###
  
Callback to be called when the user requests a resend of a verification  
code.  
  
