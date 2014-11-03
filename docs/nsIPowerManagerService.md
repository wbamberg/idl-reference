---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/power/nsIPowerManagerService.idl">Source file</a>
</div>

# nsIPowerManagerService #
<pre>  
For use with non-content code.  
  
</pre>
## Methods ##

### powerOff() ###
<pre>  
This API will power off the machine.  
  
</pre>
### reboot() ###
<pre>  
This API will completely shut down and boot the machine.  
  
</pre>
### restart() ###
<pre>  
This API will restart the Gecko processes without powering off the machine.  
  
</pre>
### addWakeLockListener(aListener) ###

### removeWakeLockListener(aListener) ###

### getWakeLockState(aTopic) ###

### newWakeLock(aTopic, aWindow) ###
<pre>  
Return a wake lock (MozWakeLock) object of aTopic associated with aWindow.  
A wake lock without associated window, e.g. used in chrome, is  
always considered invisible.  
  
</pre>