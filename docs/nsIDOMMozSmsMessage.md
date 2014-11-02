---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobilemessage/interfaces/nsIDOMMozSmsMessage.idl">Source file</a>
</div>

# nsIDOMMozSmsMessage #

## Attributes ##

### type ###
  
|type| is always "sms".  
  

### id ###

### threadId ###

### iccId ###
  
Integrated Circuit Card Identifier.  
  
Will be null if ICC is not available.  
  

### delivery ###
  
Should be "received", "sending", "sent" or "error".  
  

### deliveryStatus ###
  
Possible delivery status values for above delivery states are:  
  
"received": "success"  
"sending" : "pending", or "not-applicable" if the message was sent without  
            status report requisition.  
"sent"    : "pending", "success", "error", or "not-applicable"  
            if the message was sent without status report requisition.  
"error"   : "error"  
  

### sender ###

### receiver ###

### body ###

### messageClass ###
  
Should be "normal", "class-0", "class-1", "class-2" or "class-3".  
  

### timestamp ###

### sentTimestamp ###

### deliveryTimestamp ###

### read ###
