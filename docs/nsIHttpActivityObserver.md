---
layout: default
---

# nsIHttpActivityObserver #
  
nsIHttpActivityObserver  
  
This interface provides a way for http activities to be reported  
to observers.  
  

## Methods ##

### observeActivity(aHttpChannel, aActivityType, aActivitySubtype, aTimestamp, aExtraSizeData, aExtraStringData) ###
  
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
  

## Attributes ##

### isActive ###
  
This attribute is true when this interface is active and should  
observe http activities. When false, observeActivity() should not  
be called. It is present for compatibility reasons and should be  
implemented only by nsHttpActivityDistributor.  
  

## Constants ##

### ACTIVITY_TYPE_SOCKET_TRANSPORT ###

### ACTIVITY_TYPE_HTTP_TRANSACTION ###

### ACTIVITY_SUBTYPE_REQUEST_HEADER ###

### ACTIVITY_SUBTYPE_REQUEST_BODY_SENT ###

### ACTIVITY_SUBTYPE_RESPONSE_START ###

### ACTIVITY_SUBTYPE_RESPONSE_HEADER ###

### ACTIVITY_SUBTYPE_RESPONSE_COMPLETE ###

### ACTIVITY_SUBTYPE_TRANSACTION_CLOSE ###
