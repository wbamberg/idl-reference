---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobilemessage/interfaces/nsIRilMobileMessageDatabaseService.idl">Source file</a>
</div>

# nsIRilMobileMessageDatabaseService #

## Methods ##

### saveReceivedMessage(aMessage, aCallback) ###
  
|aMessage| Object: should contain the following properties for internal use:  
  - |type| DOMString: "sms" or "mms"  
  - |timestamp| Number: the timestamp of received message  
  - |iccId| DOMString: [optional] the ICC ID of the SIM for receiving  
                       message if available.  
  
  - If |type| == "sms", we also need:  
    - |messageClass| DOMString: the message class of received message  
    - |receiver| DOMString: the phone number of receiver  
    - |pid| Number: the TP-PID field of the SMS TPDU, default 0.  
    - |sender| DOMString: the phone number of sender  
  
  - If |type| == "mms", we also need:  
    - |delivery| DOMString: the delivery state of received message  
    - |deliveryStatus| DOMString: the delivery status of received message  
    - |receivers| DOMString Array: the phone numbers of receivers  
    - |phoneNumber| DOMString: [optional] my own phone number.  
  

### saveSendingMessage(aMessage, aCallback) ###
  
|aMessage| Object: should contain the following properties for internal use:  
  - |type| DOMString: "sms" or "mms"  
  - |sender| DOMString: the phone number of sender  
  - |timestamp| Number: the timestamp of sending message  
  - |deliveryStatusRequested| Bool: true when the delivery report is requested.  
  - |iccId| DOMString: the ICC ID of the SIM for sending message  
  
  - If |type| == "sms", we also need:  
    - |receiver| DOMString: the phone number of receiver  
  
  - If |type| == "mms", we also need:  
    - |receivers| DOMString Array: the phone numbers of receivers  
  

### setMessageDeliveryByMessageId(aMessageId, aReceiver, aDelivery, aDeliveryStatus, aEnvelopeId, aCallback) ###
  
|aMessageId| Number: the message's DB record ID.  
|aReceiver| DOMString: the phone number of receiver (for MMS; can be null).  
|aDelivery| DOMString: the new delivery value to update (can be null).  
|aDeliveryStatus| DOMString: the new delivery status to update (can be null).  
|aEnvelopeId| DOMString: the "message-id" specified in the MMS PDU headers.  
|aCallback| nsIRilMobileMessageDatabaseCallback: an optional callback.  
  

### setMessageDeliveryStatusByEnvelopeId(aEnvelopeId, aReceiver, aDeliveryStatus, aCallback) ###
  
|aEnvelopeId| DOMString: the "message-id" specified in the MMS PDU headers.  
|aReceiver| DOMString: the phone number of receiver (for MMS; can be null).  
|aDeliveryStatus| DOMString: the new delivery status to be updated (can be null).  
|aCallback| nsIRilMobileMessageDatabaseCallback: an optional callback.  
  

### setMessageReadStatusByEnvelopeId(aEnvelopeId, aReceiver, aReadStatus, aCallback) ###
  
|aEnvelopeId| DOMString: the "message-id" specified in the MMS PDU headers.  
|aReceiver| DOMString: the phone number of receiver (for MMS; can be null).  
|aReadStatus| DOMString: the new read status to be updated.  
|aCallback| nsIRilMobileMessageDatabaseCallback: an optional callback.  
  

### getMessageRecordById(aMessageId, aCallback) ###
  
|aMessageId| Number: the message's DB record ID.  
|aCallback| nsIRilMobileMessageDatabaseRecordCallback: a callback which  
  takes result flag, message record and domMessage as parameters.  
  

### getMessageRecordByTransactionId(aTransactionId, aCallback) ###
  
|aTransactionId| DOMString: the transaction ID of MMS PDU.  
|aCallback| nsIRilMobileMessageDatabaseRecordCallback: a callback which  
  takes result flag and message record as parameters.  
  

### translateCrErrorToMessageCallbackError(aCrError) ###
  
|aCrError| nsresult: the NS_ERROR defined in Components.results.  
  
  

#### Returns ####

<table>

<tr>
<td>the error code defined in nsIMobileMessageCallback  
</td>
</tr>

</table>

### saveSmsSegment(aSmsSegment, aCallback) ###
  
|aSmsSegment| jsval: Decoded Single SMS PDU.  
|aCallback| nsIRilMobileMessageDatabaseConcatenationCallback: a callback which  
  takes result flag, and complete mesage as parameters.  
  
