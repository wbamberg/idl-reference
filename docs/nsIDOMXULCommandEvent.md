---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/xul/nsIDOMXULCommandEvent.idl">Source file</a>
</div>

# nsIDOMXULCommandEvent #

## Methods ##

### initCommandEvent(typeArg, canBubbleArg, cancelableArg, viewArg, detailArg, ctrlKeyArg, altKeyArg, shiftKeyArg, metaKeyArg, sourceEvent) ###
  
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
  
