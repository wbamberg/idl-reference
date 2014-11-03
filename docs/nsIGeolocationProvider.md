---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/system/nsIGeolocationProvider.idl">Source file</a>
</div>

# nsIGeolocationProvider #
<pre>  
Interface provides location information to the nsGeolocator  
via the nsIDOMGeolocationCallback interface.  After  
startup is called, any geo location change should call  
callback.update().  
  
</pre>
## Methods ##

### startup() ###
<pre>  
Start up the provider.  This is called before any other  
method.  may be called multiple times.  
  
</pre>
### watch(callback) ###
<pre>  
watch  
When a location change is observed, notify the callback.  
  
</pre>
### shutdown() ###
<pre>  
shutdown  
Shuts down the location device.  
  
</pre>
### setHighAccuracy(enable) ###
<pre>  
hint to provide to use any amount of power to provide a better result  
  
</pre>