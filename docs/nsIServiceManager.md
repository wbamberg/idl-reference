---
layout: default
---

# nsIServiceManager #

The nsIServiceManager manager interface provides a means to obtain
global services in an application. The service manager depends on the 
repository to find and instantiate factories to obtain services.

Users of the service manager must first obtain a pointer to the global
service manager by calling NS_GetServiceManager. After that, 
they can request specific services by calling GetService. When they are
finished they can NS_RELEASE() the service as usual.

A user of a service may keep references to particular services indefinitely
and only must call Release when it shuts down.


## Methods ##

### getService ###

getServiceByContractID

Returns the instance that implements aClass or aContractID and the
interface aIID.  This may result in the instance being created.

@param aClass or aContractID : aClass or aContractID of object 
                               instance requested
@param aIID : IID of interface requested
@param result : resulting service 


### getServiceByContractID ###

### isServiceInstantiated ###

isServiceInstantiated

isServiceInstantiated will return a true if the service has already
been created, or throw otherwise

@param aClass or aContractID : aClass or aContractID of object 
                               instance requested
@param aIID : IID of interface requested
@throws NS_ERROR_SERVICE_NOT_AVAILABLE if the service hasn't been 
        instantiated
@throws NS_NOINTERFACE if the IID given isn't supported by the object


### isServiceInstantiatedByContractID ###
