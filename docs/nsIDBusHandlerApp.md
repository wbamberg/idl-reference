---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/mime/nsIMIMEInfo.idl">Source file</a>
</div>

# nsIDBusHandlerApp #
<code>  
nsIDBusHandlerApp represents local applications launched by DBus a message  
invoking a method taking a single string argument descibing a URI  
  
</code>
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
  
