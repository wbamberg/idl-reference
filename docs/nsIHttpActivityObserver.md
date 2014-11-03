---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsIHttpActivityObserver.idl">Source file</a>
</div>

# nsIHttpActivityObserver #
<pre>  
nsIHttpActivityObserver  
  
This interface provides a way for http activities to be reported  
to observers.  
  
</pre>
## Methods ##

### observeActivity(aHttpChannel, aActivityType, aActivitySubtype, aTimestamp, aExtraSizeData, aExtraStringData) ###
<pre>  
observe activity from the http transport  
  
@param aHttpChannel  
       nsISupports interface for the the http channel that  
       generated this activity  
@param aActivityType  
       The value of this aActivityType will be one of  
         ACTIVITY_TYPE_SOCKET_TRANSPORT or  
         ACTIVITY_TYPE_HTTP_TRANSACTION  
@param aActivitySubtype  
       The value of this aActivitySubtype, will be depend  
       on the value of aActivityType. When aActivityType  
       is ACTIVITY_TYPE_SOCKET_TRANSPORT  
         aActivitySubtype will be one of the  
         nsISocketTransport::STATUS_???? values defined in  
         nsISocketTransport.idl  
       OR when aActivityType  
       is ACTIVITY_TYPE_HTTP_TRANSACTION  
         aActivitySubtype will be one of the  
         nsIHttpActivityObserver::ACTIVITY_SUBTYPE_???? values  
         defined below  
@param aTimestamp  
       microseconds past the epoch of Jan 1, 1970  
@param aExtraSizeData  
       Any extra size data optionally available with  
       this activity  
@param aExtraStringData  
       Any extra string data optionally available with  
       this activity  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aHttpChannel</td>
<td>       nsISupports interface for the the http channel that  
       generated this activity  
</td>
</tr>

<tr>
<td>aActivityType</td>
<td>       The value of this aActivityType will be one of  
         ACTIVITY_TYPE_SOCKET_TRANSPORT or  
         ACTIVITY_TYPE_HTTP_TRANSACTION  
</td>
</tr>

<tr>
<td>aActivitySubtype</td>
<td>       The value of this aActivitySubtype, will be depend  
       on the value of aActivityType. When aActivityType  
       is ACTIVITY_TYPE_SOCKET_TRANSPORT  
         aActivitySubtype will be one of the  
         nsISocketTransport::STATUS_???? values defined in  
         nsISocketTransport.idl  
       OR when aActivityType  
       is ACTIVITY_TYPE_HTTP_TRANSACTION  
         aActivitySubtype will be one of the  
         nsIHttpActivityObserver::ACTIVITY_SUBTYPE_???? values  
         defined below  
</td>
</tr>

<tr>
<td>aTimestamp</td>
<td>       microseconds past the epoch of Jan 1, 1970  
</td>
</tr>

<tr>
<td>aExtraSizeData</td>
<td>       Any extra size data optionally available with  
       this activity  
</td>
</tr>

<tr>
<td>aExtraStringData</td>
<td>       Any extra string data optionally available with  
       this activity  
</td>
</tr>

</table>

## Attributes ##

### isActive ###
<pre>  
This attribute is true when this interface is active and should  
observe http activities. When false, observeActivity() should not  
be called. It is present for compatibility reasons and should be  
implemented only by nsHttpActivityDistributor.  
  
</pre>
## Constants ##

### ACTIVITY_TYPE_SOCKET_TRANSPORT ###

### ACTIVITY_TYPE_HTTP_TRANSACTION ###

### ACTIVITY_SUBTYPE_REQUEST_HEADER ###

### ACTIVITY_SUBTYPE_REQUEST_BODY_SENT ###

### ACTIVITY_SUBTYPE_RESPONSE_START ###

### ACTIVITY_SUBTYPE_RESPONSE_HEADER ###

### ACTIVITY_SUBTYPE_RESPONSE_COMPLETE ###

### ACTIVITY_SUBTYPE_TRANSACTION_CLOSE ###
