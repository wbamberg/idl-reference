---
layout: default
---

# nsIXULAppInfo #

A scriptable interface to the nsXULAppAPI structure. See nsXULAppAPI.h for
a detailed description of each attribute.


## vendor ##

@see nsXREAppData.vendor
@returns an empty string if nsXREAppData.vendor is not set.


## name ##

@see nsXREAppData.name


## ID ##

@see nsXREAppData.ID
@returns an empty string if nsXREAppData.ID is not set.


## version ##

The version of the XUL application. It is different than the
version of the XULRunner platform. Be careful about which one you want.

@see nsXREAppData.version
@returns an empty string if nsXREAppData.version is not set.


## appBuildID ##

The build ID/date of the application. For xulrunner applications,
this will be different than the build ID of the platform. Be careful
about which one you want.


## platformVersion ##

The version of the XULRunner platform.


## platformBuildID ##

The build ID/date of gecko and the XULRunner platform.


## UAName ##

@see nsXREAppData.UAName
@returns an empty string if nsXREAppData.UAName is not set.

