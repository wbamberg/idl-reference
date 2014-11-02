---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/power/nsIPowerManagerService.idl">Source file</a>
</div>
# nsIPowerManagerService #
  
For use with non-content code.  
  

## Methods ##

### powerOff() ###
  
This API will power off the machine.  
  

### reboot() ###
  
This API will completely shut down and boot the machine.  
  

### restart() ###
  
This API will restart the Gecko processes without powering off the machine.  
  

### addWakeLockListener(aListener) ###

### removeWakeLockListener(aListener) ###

### getWakeLockState(aTopic) ###

### newWakeLock(aTopic, aWindow) ###
  
Return a wake lock (MozWakeLock) object of aTopic associated with aWindow.  
A wake lock without associated window, e.g. used in chrome, is  
always considered invisible.  
  
