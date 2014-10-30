---
layout: default
---

# nsIHTMLAbsPosEditor #

## Methods ##

### absolutePositionSelection(aEnabled) ###
  
extracts the selection from the normal flow of the document and  
positions it.  
@param aEnabled [IN] true to absolutely position the selection,  
                     false to put it back in the normal flow  
  

### relativeChangeZIndex(aChange) ###
  
adds aChange to the z-index of the currently positioned element.  
@param aChange [IN] relative change to apply to current z-index  
  

### absolutelyPositionElement(aElement, aEnabled) ###
  
extracts an element from the normal flow of the document and  
positions it, and puts it back in the normal flow.  
@param aElement [IN] the element  
@param aEnabled [IN] true to absolutely position the element,  
                     false to put it back in the normal flow  
  

### setElementPosition(aElement, aX, aY) ###
  
sets the position of an element; warning it does NOT check if the  
element is already positioned or not and that's on purpose.  
@param aElement [IN] the element  
@param aX       [IN] the x position in pixels.  
@param aY       [IN] the y position in pixels.  
  

### getElementZIndex(aElement) ###
  
returns the absolute z-index of a positioned element. Never returns 'auto'.  
@return         the z-index of the element  
@param aElement [IN] the element.  
  

### setElementZIndex(aElement, aZorder) ###
  
sets the z-index of an element.  
@param aElement [IN] the element  
@param aZorder  [IN] the z-index  
  

### relativeChangeElementZIndex(aElement, aChange) ###
  
adds aChange to the z-index of an arbitrary element.  
@return         the new z-index of the element  
@param aElement [IN] the element  
@param aChange  [IN] relative change to apply to current z-index of  
                     the element  
  

### showGrabberOnElement(aElement) ###
  
shows a grabber attached to an arbitrary element. The grabber is an image  
positioned on the left hand side of the top border of the element. Dragging  
and dropping it allows to change the element's absolute position in the  
document. See chrome://editor/content/images/grabber.gif  
@param aElement [IN] the element  
  

### hideGrabber() ###
  
hide the grabber if it shown.  
  

### refreshGrabber() ###
  
refreshes the grabber if it shown, possibly updating its position or  
even hiding it.  
  

## Attributes ##

### selectionContainerAbsolutelyPositioned ###
  
true if the selection container is absolutely positioned  
  

### positionedElement ###
  
this contains the absolutely positioned element currently edited  
or null  
  

### absolutePositioningEnabled ###
  
true if Absolute Positioning handling is enabled in the editor  
  

### snapToGridEnabled ###
  
true if Snap To Grid is enabled in the editor.  
  

### gridSize ###
  
sets the grid size in pixels.  
@param aSizeInPixels [IN] the size of the grid in pixels  
  

### absolutelyPositionedSelectionContainer ###
  
returns the deepest absolutely positioned container of the selection  
if it exists or null.  
  
