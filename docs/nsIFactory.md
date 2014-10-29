---
layout: default
---

# nsIFactory #

A class factory allows the creation of nsISupports derived
components without specifying a concrete base class.  


## Methods ##

### createInstance ###

Creates an instance of a component.

@param aOuter Pointer to a component that wishes to be aggregated
              in the resulting instance. This will be nullptr if no
              aggregation is requested.
@param iid    The IID of the interface being requested in
              the component which is being currently created.
@param result [out] Pointer to the newly created instance, if successful.
@throws NS_NOINTERFACE - Interface not accessible.
@throws NS_ERROR_NO_AGGREGATION - if an 'outer' object is supplied, but the
                                  component is not aggregatable.
        NS_ERROR* - Method failure.


### lockFactory ###

LockFactory provides the client a way to keep the component
in memory until it is finished with it. The client can call
LockFactory(PR_TRUE) to lock the factory and LockFactory(PR_FALSE)
to release the factory.	 

@param lock - Must be PR_TRUE or PR_FALSE
@throws NS_ERROR* - Method failure.

