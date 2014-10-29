---
layout: default
---

# nsIGeolocationProvider #

Interface provides location information to the nsGeolocator
via the nsIDOMGeolocationCallback interface.  After
startup is called, any geo location change should call
callback.update().


## Methods ##

### startup ###

Start up the provider.  This is called before any other
method.  may be called multiple times.


### watch ###

watch
When a location change is observed, notify the callback.


### shutdown ###

shutdown
Shuts down the location device.


### setHighAccuracy ###

hint to provide to use any amount of power to provide a better result

