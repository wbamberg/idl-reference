---
layout: default
---

# nsISyncMessageSender #

## Methods ##

### sendSyncMessage ###
  
Like |sendAsyncMessage()|, except blocks the sender until all  
listeners of the message have been invoked.  Returns an array  
containing return values from each listener invoked.  
  

### sendRpcMessage ###
  
Like |sendSyncMessage()|, except re-entrant. New RPC messages may be  
issued even if, earlier on the call stack, we are waiting for a reply  
to an earlier sendRpcMessage() call.  
  
Both sendSyncMessage and sendRpcMessage will block until a reply is  
received, but they may be temporarily interrupted to process an urgent  
incoming message (such as a CPOW request).  
  
