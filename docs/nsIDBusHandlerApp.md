---
layout: default
---

# nsIDBusHandlerApp #
  
nsIDBusHandlerApp represents local applications launched by DBus a message  
invoking a method taking a single string argument descibing a URI  
  

## Attributes ##

### service ###
  
Service defines the dbus service that should handle this protocol.  
If its not set,  NS_ERROR_FAILURE will be returned by LaunchWithURI  
  

### objectPath ###
  
Objpath defines the object path of the dbus service that should handle   
this protocol. If its not set,  NS_ERROR_FAILURE will be returned   
by LaunchWithURI  
  

### dBusInterface ###
  
DBusInterface defines the interface of the dbus service that should   
handle this protocol. If its not set,  NS_ERROR_FAILURE will be    
returned by LaunchWithURI  
  

### method ###
  
Method defines the dbus method that should be invoked to handle this   
protocol. If its not set,  NS_ERROR_FAILURE will be returned by   
LaunchWithURI  
  
