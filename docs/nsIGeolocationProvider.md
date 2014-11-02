---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/system/nsIGeolocationProvider.idl">Source file</a>
</div>

# nsIGeolocationProvider #
  
Interface provides location information to the nsGeolocator  
via the nsIDOMGeolocationCallback interface.  After  
startup is called, any geo location change should call  
callback.update().  
  

## Methods ##

### startup() ###
  
Start up the provider.  This is called before any other  
method.  may be called multiple times.  
  

### watch(callback) ###
  
watch  
When a location change is observed, notify the callback.  
  

### shutdown() ###
  
shutdown  
Shuts down the location device.  
  

### setHighAccuracy(enable) ###
  
hint to provide to use any amount of power to provide a better result  
  
