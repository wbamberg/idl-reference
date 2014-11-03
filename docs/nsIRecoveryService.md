---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/hal/gonk/nsIRecoveryService.idl">Source file</a>
</div>

# nsIRecoveryService #

## Methods ##

### factoryReset(reason) ###
<pre>  
Uses recovery to wipe the data and cache partitions. If this call is  
successful, the device should reboot before the function call ever returns.  
  
@throws NS_ERROR_FAILURE when rebooting into recovery fails for some reason.  
  
</pre>
### installFotaUpdate(updatePath) ###
<pre>  
Use recovery to install an OTA update.zip. If this call is  
successful, the device should reboot before the function call ever returns.  
  
@throws NS_ERROR_FAILURE when rebooting into recovery fails for some reason.  
  
</pre>
### getFotaUpdateStatus() ###
<pre>  
@return The status of the last FOTA update. One of FOTA_UPDATE_UNKNOWN,  
        FOTA_UPDATE_FAIL, FOTA_UPDATE_SUCCESS.  
  
</pre>
#### Returns ####

<table>

<tr>
<td>The status of the last FOTA update. One of FOTA_UPDATE_UNKNOWN,  
        FOTA_UPDATE_FAIL, FOTA_UPDATE_SUCCESS.  
</td>
</tr>

</table>

## Constants ##

### FOTA_UPDATE_UNKNOWN ###
<pre>  
Possible values of fotaStatus.result. These should stay in sync with  
librecovery/librecovery.h  
  
</pre>
### FOTA_UPDATE_FAIL ###

### FOTA_UPDATE_SUCCESS ###
