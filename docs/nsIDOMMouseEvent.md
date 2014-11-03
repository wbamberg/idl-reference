---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/events/nsIDOMMouseEvent.idl">Source file</a>
</div>

# nsIDOMMouseEvent #
<pre>  
The nsIDOMMouseEvent interface is the datatype for all mouse events  
in the Document Object Model.  
  
For more information on this interface please see  
http://www.w3.org/TR/DOM-Level-2-Events/  
  
</pre>
## Methods ##

### initMouseEvent(typeArg, canBubbleArg, cancelableArg, viewArg, detailArg, screenXArg, screenYArg, clientXArg, clientYArg, ctrlKeyArg, altKeyArg, shiftKeyArg, metaKeyArg, buttonArg, relatedTargetArg) ###

### initNSMouseEvent(typeArg, canBubbleArg, cancelableArg, viewArg, detailArg, screenXArg, screenYArg, clientXArg, clientYArg, ctrlKeyArg, altKeyArg, shiftKeyArg, metaKeyArg, buttonArg, relatedTargetArg, pressure, inputSourceArg) ###

### getModifierState(keyArg) ###

## Attributes ##

### screenX ###

### screenY ###

### mozMovementX ###

### mozMovementY ###

### clientX ###

### clientY ###

### ctrlKey ###

### shiftKey ###

### altKey ###

### metaKey ###

### button ###

### buttons ###

### relatedTarget ###

### mozPressure ###

### mozInputSource ###

## Constants ##

### MOZ_SOURCE_UNKNOWN ###

### MOZ_SOURCE_MOUSE ###

### MOZ_SOURCE_PEN ###

### MOZ_SOURCE_ERASER ###

### MOZ_SOURCE_CURSOR ###

### MOZ_SOURCE_TOUCH ###

### MOZ_SOURCE_KEYBOARD ###
