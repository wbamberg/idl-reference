---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/system/nsIGeolocationProvider.idl">Source file</a>
</div>

# nsIGeolocationProvider #
<code>  
Interface provides location information to the nsGeolocator  
via the nsIDOMGeolocationCallback interface.  After  
startup is called, any geo location change should call  
callback.update().  
  
</code>
## Methods ##

### startup() ###
<code>  
Start up the provider.  This is called before any other  
method.  may be called multiple times.  
  
</code>
### watch(callback) ###
<code>  
watch  
When a location change is observed, notify the callback.  
  
</code>
### shutdown() ###
<code>  
shutdown  
Shuts down the location device.  
  
</code>
### setHighAccuracy(enable) ###
<code>  
hint to provide to use any amount of power to provide a better result  
  
</code>