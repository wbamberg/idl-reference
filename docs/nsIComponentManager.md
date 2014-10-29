---
layout: default
---

# nsIComponentManager #

## getClassObject ##

getClassObject

Returns the factory object that can be used to create instances of
CID aClass

@param aClass The classid of the factory that is being requested


## getClassObjectByContractID ##

getClassObjectByContractID

Returns the factory object that can be used to create instances of
CID aClass

@param aClass The classid of the factory that is being requested


## createInstance ##

createInstance

Create an instance of the CID aClass and return the interface aIID.

@param aClass : ClassID of object instance requested
@param aDelegate : Used for aggregation
@param aIID : IID of interface requested


## createInstanceByContractID ##

createInstanceByContractID

Create an instance of the CID that implements aContractID and return the
interface aIID. 

@param aContractID : aContractID of object instance requested
@param aDelegate : Used for aggregation
@param aIID : IID of interface requested


## addBootstrappedManifestLocation ##

addBootstrappedManifestLocation

Adds a bootstrapped manifest location on runtime.

@param aLocation : A directory where chrome.manifest resides,
                   or an XPI with it on the root.


## removeBootstrappedManifestLocation ##

removeBootstrappedManifestLocation

Removes a bootstrapped manifest location on runtime.

@param aLocation : A directory where chrome.manifest resides,
                   or an XPI with it on the root.


## getManifestLocations ##

getManifestLocations

Get an array of nsIURIs of all registered and builtin manifest locations.

