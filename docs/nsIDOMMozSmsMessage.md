---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobilemessage/interfaces/nsIDOMMozSmsMessage.idl">Source file</a>
</div>

# nsIDOMMozSmsMessage #

## Attributes ##

### type ###
<pre>  
|type| is always "sms".  
  
</pre>
### id ###

### threadId ###

### iccId ###
<pre>  
Integrated Circuit Card Identifier.  
  
Will be null if ICC is not available.  
  
</pre>
### delivery ###
<pre>  
Should be "received", "sending", "sent" or "error".  
  
</pre>
### deliveryStatus ###
<pre>  
Possible delivery status values for above delivery states are:  
  
"received": "success"  
"sending" : "pending", or "not-applicable" if the message was sent without  
            status report requisition.  
"sent"    : "pending", "success", "error", or "not-applicable"  
            if the message was sent without status report requisition.  
"error"   : "error"  
  
</pre>
### sender ###

### receiver ###

### body ###

### messageClass ###
<pre>  
Should be "normal", "class-0", "class-1", "class-2" or "class-3".  
  
</pre>
### timestamp ###

### sentTimestamp ###

### deliveryTimestamp ###

### read ###
