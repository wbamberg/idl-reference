---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/system/nsIGeolocationProvider.idl">Source file</a>
</div>

# nsIGeolocationUpdate #
<code>  
  
Interface provides a way for a geolocation provider to  
notify the system that a new location is available.  
  
</code>
## Methods ##

### update(position) ###
<code>  
Notify the geolocation service that a new geolocation  
has been discovered.  
This must be called on the main thread  
  
</code>
### locationUpdatePending() ###
<code>  
Notify the geolocation service that the location has  
potentially changed, and thus a new position is in the  
process of being acquired.  
  
</code>
### notifyError(error) ###
<code>  
Notify the geolocation service of an error.  
This must be called on the main thread.  
The parameter refers to one of the constants in the  
nsIDOMGeoPositionError interface.  
Use this to report spurious errors coming from the  
provider; for errors occurring inside the methods in  
the nsIGeolocationProvider interface, just use the return  
value.  
  
</code>