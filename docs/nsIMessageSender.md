---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIMessageManager.idl">Source file</a>
</div>

# nsIMessageSender #
<code>  
Message "senders" have a single "other side" to which messages are  
sent.  For example, a child-process message manager will send  
messages that are only delivered to its one parent-process message  
manager.  
  
</code>
## Methods ##

### sendAsyncMessage(messageName, obj, objects, principal) ###
<code>  
Send |messageName| and |obj| to the "other side" of this message  
manager.  This invokes listeners who registered for  
|messageName|.  
  
See nsIMessageListener::receiveMessage() for the format of the  
data delivered to listeners.  
@throws NS_ERROR_NOT_INITIALIZED if the sender is not initialized.  For  
        example, we will throw NS_ERROR_NOT_INITIALIZED if we try to send  
        a message to a cross-process frame but the other process has not  
        yet been set up.  
@throws NS_ERROR_FAILURE when the message receiver cannot be found.  For  
        example, we will throw NS_ERROR_FAILURE if we try to send a message  
        to a cross-process frame whose process has crashed.  
  
</code>