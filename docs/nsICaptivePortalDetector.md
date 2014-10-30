---
layout: default
---

# nsICaptivePortalDetector #

## Methods ##

### checkCaptivePortal(ifname, callback) ###
  
Perform captive portal detection on specific network interface.  
@param ifname The name of network interface, exception will be thrwon  
              if the same interface has unfinished request.  
@param callback Callbacks when detection procedure starts and finishes.  
  

### abort(ifname) ###
  
Abort captive portal detection for specific network interface  
due to system failure, callback will not be invoked.  
@param ifname The name of network interface.  
  

### cancelLogin(eventId) ###
  
Cancel captive portal login procedure by user, callback will be invoked.  
@param eventId Login event id provided in |captive-portal-login| event.  
  

### finishPreparation(ifname) ###
  
Notify prepare phase is finished, routing and dns must be ready for sending  
out XMLHttpRequest. this is callback for CaptivePortalDetector API user.  
@param ifname The name of network interface, must be unique.  
  
