---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/telephony/nsITelephonyService.idl">Source file</a>
</div>

# nsITelephonyDialCallback #
<pre>  
A callback interface for handling asynchronous response for telephony.dial.  
  
</pre>
## Methods ##

### notifyDialMMI(serviceCode) ###
<pre>  
Called when a dial request is treated as an MMI code and it is about to  
process the request.  
  
@param serviceCode  
       MMI service code key string that defined in MMI_KS_SC_*  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>serviceCode</td>
<td>       MMI service code key string that defined in MMI_KS_SC_*  
</td>
</tr>

</table>

### notifyDialCallSuccess(callIndex, number) ###
<pre>  
Called when a dial request is treated as a call setup and the result  
succeeds.  
  
@param callIndex  
       Call index from RIL.  
@param number  
       Dialed out phone number (ex: Temporary CLIR prefix will be removed)  
  
</pre>
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
<pre>  
Called when a MMI code request succeeds.  
The function should only be called after notifyDialMMI.  
  
@param result  
       Result of the request. See MozMMIResult.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>result</td>
<td>       Result of the request. See MozMMIResult.  
</td>
</tr>

</table>

### notifyDialMMIError(error) ###
<pre>  
Called when a MMI code request fails.  
The function should only be called after notifyDialMMI.  
  
</pre>
### notifyDialMMIErrorWithInfo(error, info) ###
