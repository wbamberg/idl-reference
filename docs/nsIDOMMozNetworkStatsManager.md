---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/network/interfaces/nsIDOMNetworkStatsManager.idl">Source file</a>
</div>
# nsIDOMMozNetworkStatsManager #

## Methods ##

### getSamples(network, start, end, options) ###
  
Find samples between two dates start and end, both included.  
  
If options is provided, per-app or per-system service usage will be  
retrieved; otherwise the target will be overall system usage.  
  
If success, the request result will be an nsIDOMMozNetworkStats object.  
  

### addAlarm(network, threshold, options) ###
  
Install an alarm on a network. The network must be in the return of  
getAvailableNetworks() otherwise an "InvalidNetwork" exception will  
be raised.  
  
When total data usage reaches threshold bytes, a "networkstats-alarm"  
system message is sent to the application, where the optional parameter  
|data| must be a cloneable object.  
  
If success, the |result| field of the DOMRequest keeps the alarm Id.  
  

### getAllAlarms(network) ###
  
Obtain all alarms for those networks returned by getAvailableNetworks().  
If a network is provided, only retrieves the alarms for that network.  
The network must be one of those returned by getAvailebleNetworks() or an  
"InvalidNetwork" exception will be raised.  
  
Each alarm object has the same fields as that in the system message:  
 - alarmId  
 - network  
 - threshold  
 - data  
  

### removeAlarms(alarmId) ###
  
Remove all network alarms. If an |alarmId| is provided, then only that  
alarm is removed.  
  

### clearStats(network) ###
  
Remove all stats related with the provided network from DB.  
  

### clearAllStats() ###
  
Remove all stats in the database.  
  

### getAvailableNetworks() ###
  
Return available networks that used to be saved in the database.  
  

### getAvailableServiceTypes() ###
  
Return available service types that used to be saved in the database.  
  

## Attributes ##

### sampleRate ###
  
Minimum time in milliseconds between samples stored in the database.  
  

### maxStorageAge ###
  
Time in milliseconds recorded by the API until present time. All samples  
older than maxStorageAge from now are deleted.  
  

## Constants ##

### WIFI ###
  
Constants for known interface types.  
  

### MOBILE ###
