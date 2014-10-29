---
layout: default
---

# nsIPowerManagerService #

For use with non-content code.


## Methods ##

### powerOff ###

This API will power off the machine.


### reboot ###

This API will completely shut down and boot the machine.


### restart ###

This API will restart the Gecko processes without powering off the machine.


### addWakeLockListener ###

### removeWakeLockListener ###

### getWakeLockState ###

### newWakeLock ###

Return a wake lock (MozWakeLock) object of aTopic associated with aWindow.
A wake lock without associated window, e.g. used in chrome, is
always considered invisible.

