---
layout: default
---

# nsIHTMLObjectResizer #

## Methods ##

### showResizers(aResizedElement) ###
  
Shows active resizers around an element's frame  
@param aResizedElement [IN] a DOM Element  
  

### hideResizers() ###
  
Hide resizers if they are visible  
  

### refreshResizers() ###
  
Refresh visible resizers  
  

### mouseDown(aX, aY, aTarget, aMouseEvent) ###
  
event callback when a mouse button is pressed  
@param aX      [IN] horizontal position of the pointer  
@param aY      [IN] vertical position of the pointer  
@param aTarget [IN] the element triggering the event  
@param aMouseEvent [IN] the event  
  

### mouseUp(aX, aY, aTarget) ###
  
event callback when a mouse button is released  
@param aX      [IN] horizontal position of the pointer  
@param aY      [IN] vertical position of the pointer  
@param aTarget [IN] the element triggering the event  
  

### mouseMove(aMouseEvent) ###
  
event callback when the mouse pointer is moved  
@param aMouseEvent [IN] the event  
  

### addObjectResizeEventListener(aListener) ###
  
Creates a resize listener that can be used to get notifications  
that the user started to resize an object or finalized such an operation  
@param aListener [IN] an instance of nsIHTMLObjectResizeListener  
  

### removeObjectResizeEventListener(aListener) ###
  
Deletes a resize listener  
@param aListener [IN] an instance of nsIHTMLObjectResizeListener  
  

## Attributes ##

### resizedObject ###
  
the element currently displaying resizers  
  

### objectResizingEnabled ###
  
a boolean indicating if object resizing is enabled in the editor  
  

## Constants ##

### eTopLeft ###

### eTop ###

### eTopRight ###

### eLeft ###

### eRight ###

### eBottomLeft ###

### eBottom ###

### eBottomRight ###
