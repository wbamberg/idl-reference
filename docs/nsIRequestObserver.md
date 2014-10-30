---
layout: default
---

# nsIRequestObserver #
  
nsIRequestObserver  
  

## Methods ##

### onStartRequest ###
  
Called to signify the beginning of an asynchronous request.  
  
@param aRequest request being observed  
@param aContext user defined context  
  
An exception thrown from onStartRequest has the side-effect of  
causing the request to be canceled.  
  

### onStopRequest ###
  
Called to signify the end of an asynchronous request.  This  
call is always preceded by a call to onStartRequest.  
  
@param aRequest request being observed  
@param aContext user defined context  
@param aStatusCode reason for stopping (NS_OK if completed successfully)  
  
An exception thrown from onStopRequest is generally ignored.  
  
