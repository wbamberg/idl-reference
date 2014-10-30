---
layout: default
---

# nsIMessageBroadcaster #
  
Message "broadcasters" don't have a single "other side" that they  
send messages to, but rather a set of subordinate message managers.  
For example, broadcasting a message through a window message  
manager will broadcast the message to all frame message managers  
within its window.  
  

## Methods ##

### broadcastAsyncMessage ###
  
Like |sendAsyncMessage()|, but also broadcasts this message to  
all "child" message managers of this message manager.  See long  
comment above for details.  
  
WARNING: broadcasting messages can be very expensive and leak  
sensitive data.  Use with extreme caution.  
  

### getChildAt ###
  
Return a single subordinate message manager.  
  

## Attributes ##

### childCount ###
  
Number of subordinate message managers.  
  
