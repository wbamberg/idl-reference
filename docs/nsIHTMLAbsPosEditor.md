---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIHTMLAbsPosEditor.idl">Source file</a>
</div>

# nsIHTMLAbsPosEditor #

## Methods ##

### absolutePositionSelection(aEnabled) ###
<code>  
extracts the selection from the normal flow of the document and  
positions it.  
@param aEnabled [IN] true to absolutely position the selection,  
                     false to put it back in the normal flow  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aEnabled</td>
<td>[IN] true to absolutely position the selection,  
                     false to put it back in the normal flow  
</td>
</tr>

</table>

### relativeChangeZIndex(aChange) ###
<code>  
adds aChange to the z-index of the currently positioned element.  
@param aChange [IN] relative change to apply to current z-index  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aChange</td>
<td>[IN] relative change to apply to current z-index  
</td>
</tr>

</table>

### absolutelyPositionElement(aElement, aEnabled) ###
<code>  
extracts an element from the normal flow of the document and  
positions it, and puts it back in the normal flow.  
@param aElement [IN] the element  
@param aEnabled [IN] true to absolutely position the element,  
                     false to put it back in the normal flow  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element  
</td>
</tr>

<tr>
<td>aEnabled</td>
<td>[IN] true to absolutely position the element,  
                     false to put it back in the normal flow  
</td>
</tr>

</table>

### setElementPosition(aElement, aX, aY) ###
<code>  
sets the position of an element; warning it does NOT check if the  
element is already positioned or not and that's on purpose.  
@param aElement [IN] the element  
@param aX       [IN] the x position in pixels.  
@param aY       [IN] the y position in pixels.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element  
</td>
</tr>

<tr>
<td>aX</td>
<td>[IN] the x position in pixels.  
</td>
</tr>

<tr>
<td>aY</td>
<td>[IN] the y position in pixels.  
</td>
</tr>

</table>

### getElementZIndex(aElement) ###
<code>  
returns the absolute z-index of a positioned element. Never returns 'auto'.  
@return         the z-index of the element  
@param aElement [IN] the element.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the z-index of the element  
</td>
</tr>

</table>

### setElementZIndex(aElement, aZorder) ###
<code>  
sets the z-index of an element.  
@param aElement [IN] the element  
@param aZorder  [IN] the z-index  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element  
</td>
</tr>

<tr>
<td>aZorder</td>
<td>[IN] the z-index  
</td>
</tr>

</table>

### relativeChangeElementZIndex(aElement, aChange) ###
<code>  
adds aChange to the z-index of an arbitrary element.  
@return         the new z-index of the element  
@param aElement [IN] the element  
@param aChange  [IN] relative change to apply to current z-index of  
                     the element  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element  
</td>
</tr>

<tr>
<td>aChange</td>
<td>[IN] relative change to apply to current z-index of  
                     the element  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the new z-index of the element  
</td>
</tr>

</table>

### showGrabberOnElement(aElement) ###
<code>  
shows a grabber attached to an arbitrary element. The grabber is an image  
positioned on the left hand side of the top border of the element. Dragging  
and dropping it allows to change the element's absolute position in the  
document. See chrome://editor/content/images/grabber.gif  
@param aElement [IN] the element  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>[IN] the element  
</td>
</tr>

</table>

### hideGrabber() ###
<code>  
hide the grabber if it shown.  
  
</code>
### refreshGrabber() ###
<code>  
refreshes the grabber if it shown, possibly updating its position or  
even hiding it.  
  
</code>
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
  
