---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIMessageManager.idl">Source file</a>
</div>

# nsIMessageListenerManager #

## Methods ##

### addMessageListener(messageName, listener) ###
  
Register |listener| to receive |messageName|.  All listener  
callbacks for a particular message are invoked when that message  
is received.  
  
The message manager holds a strong ref to |listener|.  
  
If the same listener registers twice for the same message, the  
second registration is ignored.  
  

### removeMessageListener(messageName, listener) ###
  
Undo an |addMessageListener| call -- that is, calling this causes us to no  
longer invoke |listener| when |messageName| is received.  
  
removeMessageListener does not remove a message listener added via  
addWeakMessageListener; use removeWeakMessageListener for that.  
  

### addWeakMessageListener(messageName, listener) ###
  
This is just like addMessageListener, except the message manager holds a  
weak ref to |listener|.  
  
If you have two weak message listeners for the same message, they may be  
called in any order.  
  

### removeWeakMessageListener(messageName, listener) ###
  
This undoes an |addWeakMessageListener| call.  
  

### markForCC() ###
