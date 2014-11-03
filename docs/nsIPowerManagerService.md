---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/power/nsIPowerManagerService.idl">Source file</a>
</div>

# nsIPowerManagerService #
<code>  
For use with non-content code.  
  
</code>
## Methods ##

### powerOff() ###
<code>  
This API will power off the machine.  
  
</code>
### reboot() ###
<code>  
This API will completely shut down and boot the machine.  
  
</code>
### restart() ###
<code>  
This API will restart the Gecko processes without powering off the machine.  
  
</code>
### addWakeLockListener(aListener) ###

### removeWakeLockListener(aListener) ###

### getWakeLockState(aTopic) ###

### newWakeLock(aTopic, aWindow) ###
<code>  
Return a wake lock (MozWakeLock) object of aTopic associated with aWindow.  
A wake lock without associated window, e.g. used in chrome, is  
always considered invisible.  
  
</code>