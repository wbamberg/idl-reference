---
layout: default
---

# nsIDOMXULCommandEvent #

## Methods ##

### initCommandEvent ###
  
Creates a new command event with the given attributes.  
  

## Attributes ##

### ctrlKey ###
  
Command events support the same set of modifier keys as mouse and key  
events.  
  

### shiftKey ###

### altKey ###

### metaKey ###

### sourceEvent ###
  
If the command event was redispatched because of a command= attribute  
on the original target, sourceEvent will be set to the original DOM Event.  
Otherwise, sourceEvent is null.  
  
