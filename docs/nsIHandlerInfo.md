---
layout: default
---

# nsIHandlerInfo #
  
nsIHandlerInfo gives access to the information about how a given protocol  
scheme or MIME-type is handled.  
  

## Methods ##

### launchWithURI(aURI, aWindowContext) ###
  
Launches the application with the specified URI, in a way that  
depends on the value of preferredAction. preferredAction must be  
useHelperApp or useSystemDefault.  
   
@note Only the URI scheme is used to determine how to launch.  This is  
essentially a pass-by-value operation.  This means that in the case of  
a file: URI, the handler that is registered for file: will be launched  
and our code will not make any decision based on the content-type or  
extension, though the invoked file: handler is free to do so.   
  
@param aURI  
       The URI to launch this application with  
  
@param aWindowContext   
       The window to parent the dialog against, and, if a web handler  
       is chosen, it is loaded in this window as well.  See   
       nsIHandlerApp.launchWithURI for more details.  
  
@throw NS_ERROR_INVALID_ARG if preferredAction is not valid for this  
call. Other exceptions may be thrown.  
  

## Attributes ##

### type ###
  
The type of this handler info.  For MIME handlers, this is the MIME type.  
For protocol handlers, it's the scheme.  
  
@return String representing the type.  
  

### description ###
  
A human readable description of the handler type  
  

### preferredApplicationHandler ###
  
The application the user has said they want associated with this content  
type. This is not always guaranteed to be set!!  
  

### possibleApplicationHandlers ###
  
Applications that can handle this content type.  
  
The list will include the preferred handler, if any.  Elements of this  
array are nsIHandlerApp objects, and this attribute will always reference  
an array, whether or not there are any possible handlers.  If there are  
no possible handlers, the array will contain no elements, so just check  
its length (nsIArray::length) to see if there are any possible handlers.  
  

### hasDefaultHandler ###
  
Indicates whether a default application handler exists,  
i.e. whether launchWithFile with action = useSystemDefault is possible  
and defaultDescription will contain usable information.  
  

### defaultDescription ###
  
A pretty name description of the associated default application. Only  
usable if hasDefaultHandler is true.  
  

### preferredAction ###
  
preferredAction is how the user specified they would like to handle  
this content type: save to disk, use specified helper app, use OS  
default handler or handle using navigator; possible value constants  
listed below  
  

### alwaysAskBeforeHandling ###
  
alwaysAskBeforeHandling: if true, we should always give the user a  
dialog asking how to dispose of this content.  
  

## Constants ##

### saveToDisk ###

### alwaysAsk ###
  
Used to indicate that we know nothing about what to do with this.  You  
could consider this to be not initialized.  
  

### useHelperApp ###

### handleInternally ###

### useSystemDefault ###
