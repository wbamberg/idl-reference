---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/captivedetect/nsICaptivePortalDetector.idl">Source file</a>
</div>
# nsICaptivePortalDetector #

## Methods ##

### checkCaptivePortal(ifname, callback) ###
  
Perform captive portal detection on specific network interface.  
@param ifname The name of network interface, exception will be thrwon  
              if the same interface has unfinished request.  
@param callback Callbacks when detection procedure starts and finishes.  
  

#### Parameters ####

<table>

<tr>
<td>ifname</td>
<td>The name of network interface, exception will be thrwon  
              if the same interface has unfinished request.  
</td>
</tr>

<tr>
<td>callback</td>
<td>Callbacks when detection procedure starts and finishes.  
</td>
</tr>

</table>

### abort(ifname) ###
  
Abort captive portal detection for specific network interface  
due to system failure, callback will not be invoked.  
@param ifname The name of network interface.  
  

#### Parameters ####

<table>

<tr>
<td>ifname</td>
<td>The name of network interface.  
</td>
</tr>

</table>

### cancelLogin(eventId) ###
  
Cancel captive portal login procedure by user, callback will be invoked.  
@param eventId Login event id provided in |captive-portal-login| event.  
  

#### Parameters ####

<table>

<tr>
<td>eventId</td>
<td>Login event id provided in |captive-portal-login| event.  
</td>
</tr>

</table>

### finishPreparation(ifname) ###
  
Notify prepare phase is finished, routing and dns must be ready for sending  
out XMLHttpRequest. this is callback for CaptivePortalDetector API user.  
@param ifname The name of network interface, must be unique.  
  

#### Parameters ####

<table>

<tr>
<td>ifname</td>
<td>The name of network interface, must be unique.  
</td>
</tr>

</table>
