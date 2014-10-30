---
layout: default
---

# nsIConsoleAPIStorage #

## Methods ##

### getEvents ###
  
Get the events array by inner window ID or all events from all windows.  
  
@param string [aId]  
       Optional, the inner window ID for which you want to get the array of  
       cached events.  
@returns array  
         The array of cached events for the given window. If no |aId| is  
         given this function returns all of the cached events, from any  
         window.  
  

### recordEvent ###
  
Record an event associated with the given window ID.  
  
@param string aId  
       The ID of the inner window for which the event occurred or "jsm" for  
       messages logged from JavaScript modules..  
@param object aEvent  
       A JavaScript object you want to store.  
  

### clearEvents ###
  
Clear storage data for the given window.  
  
@param string [aId]  
       Optional, the inner window ID for which you want to clear the  
       messages. If this is not specified all of the cached messages are  
       cleared, from all window objects.  
  
