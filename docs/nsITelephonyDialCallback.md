---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/telephony/nsITelephonyService.idl">Source file</a>
</div>

# nsITelephonyDialCallback #
<code>  
A callback interface for handling asynchronous response for telephony.dial.  
  
</code>
## Methods ##

### notifyDialMMI(serviceCode) ###
<code>  
Called when a dial request is treated as an MMI code and it is about to  
process the request.  
  
@param serviceCode  
       MMI service code key string that defined in MMI_KS_SC_*  
  
</code>
#### Parameters ####

<table>

<tr>
<td>serviceCode</td>
<td>       MMI service code key string that defined in MMI_KS_SC_*  
</td>
</tr>

</table>

### notifyDialCallSuccess(callIndex, number) ###
<code>  
Called when a dial request is treated as a call setup and the result  
succeeds.  
  
@param callIndex  
       Call index from RIL.  
@param number  
       Dialed out phone number (ex: Temporary CLIR prefix will be removed)  
  
</code>
#### Parameters ####

<table>

<tr>
<td>callIndex</td>
<td>       Call index from RIL.  
</td>
</tr>

<tr>
<td>number</td>
<td>       Dialed out phone number (ex: Temporary CLIR prefix will be removed)  
</td>
</tr>

</table>

### notifyDialMMISuccess(result) ###
<code>  
Called when a MMI code request succeeds.  
The function should only be called after notifyDialMMI.  
  
@param result  
       Result of the request. See MozMMIResult.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>result</td>
<td>       Result of the request. See MozMMIResult.  
</td>
</tr>

</table>

### notifyDialMMIError(error) ###
<code>  
Called when a MMI code request fails.  
The function should only be called after notifyDialMMI.  
  
</code>
### notifyDialMMIErrorWithInfo(error, info) ###
