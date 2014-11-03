---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/mime/nsIMIMEInfo.idl">Source file</a>
</div>

# nsIDBusHandlerApp #
<pre>  
nsIDBusHandlerApp represents local applications launched by DBus a message  
invoking a method taking a single string argument descibing a URI  
  
</pre>
## Attributes ##

### service ###
<pre>  
Service defines the dbus service that should handle this protocol.  
If its not set,  NS_ERROR_FAILURE will be returned by LaunchWithURI  
  
</pre>
### objectPath ###
<pre>  
Objpath defines the object path of the dbus service that should handle   
this protocol. If its not set,  NS_ERROR_FAILURE will be returned   
by LaunchWithURI  
  
</pre>
### dBusInterface ###
<pre>  
DBusInterface defines the interface of the dbus service that should   
handle this protocol. If its not set,  NS_ERROR_FAILURE will be    
returned by LaunchWithURI  
  
</pre>
### method ###
<pre>  
Method defines the dbus method that should be invoked to handle this   
protocol. If its not set,  NS_ERROR_FAILURE will be returned by   
LaunchWithURI  
  
</pre>