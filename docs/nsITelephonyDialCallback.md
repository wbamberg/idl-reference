---
layout: default
---

# nsITelephonyDialCallback #
  
A callback interface for handling asynchronous response for telephony.dial.  
  

## Methods ##

### notifyDialMMI(serviceCode) ###
  
Called when a dial request is treated as an MMI code and it is about to  
process the request.  
  
@param serviceCode  
       MMI service code key string that defined in MMI_KS_SC_*  
  

### notifyDialCallSuccess(callIndex, number) ###
  
Called when a dial request is treated as a call setup and the result  
succeeds.  
  
@param callIndex  
       Call index from RIL.  
@param number  
       Dialed out phone number (ex: Temporary CLIR prefix will be removed)  
  

### notifyDialMMISuccess(result) ###
  
Called when a MMI code request succeeds.  
The function should only be called after notifyDialMMI.  
  
@param result  
       Result of the request. See MozMMIResult.  
  

### notifyDialMMIError(error) ###
  
Called when a MMI code request fails.  
The function should only be called after notifyDialMMI.  
  

### notifyDialMMIErrorWithInfo(error, info) ###
