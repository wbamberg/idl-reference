---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIHTMLObjectResizer.idl">Source file</a>
</div>

# nsIHTMLObjectResizer #

## Methods ##

### showResizers(aResizedElement) ###
<code>  
Shows active resizers around an element's frame  
@param aResizedElement [IN] a DOM Element  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aResizedElement</td>
<td>[IN] a DOM Element  
</td>
</tr>

</table>

### hideResizers() ###
<code>  
Hide resizers if they are visible  
  
</code>
### refreshResizers() ###
<code>  
Refresh visible resizers  
  
</code>
### mouseDown(aX, aY, aTarget, aMouseEvent) ###
<code>  
event callback when a mouse button is pressed  
@param aX      [IN] horizontal position of the pointer  
@param aY      [IN] vertical position of the pointer  
@param aTarget [IN] the element triggering the event  
@param aMouseEvent [IN] the event  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aX</td>
<td>[IN] horizontal position of the pointer  
</td>
</tr>

<tr>
<td>aY</td>
<td>[IN] vertical position of the pointer  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>[IN] the element triggering the event  
</td>
</tr>

<tr>
<td>aMouseEvent</td>
<td>[IN] the event  
</td>
</tr>

</table>

### mouseUp(aX, aY, aTarget) ###
<code>  
event callback when a mouse button is released  
@param aX      [IN] horizontal position of the pointer  
@param aY      [IN] vertical position of the pointer  
@param aTarget [IN] the element triggering the event  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aX</td>
<td>[IN] horizontal position of the pointer  
</td>
</tr>

<tr>
<td>aY</td>
<td>[IN] vertical position of the pointer  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>[IN] the element triggering the event  
</td>
</tr>

</table>

### mouseMove(aMouseEvent) ###
<code>  
event callback when the mouse pointer is moved  
@param aMouseEvent [IN] the event  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aMouseEvent</td>
<td>[IN] the event  
</td>
</tr>

</table>

### addObjectResizeEventListener(aListener) ###
<code>  
Creates a resize listener that can be used to get notifications  
that the user started to resize an object or finalized such an operation  
@param aListener [IN] an instance of nsIHTMLObjectResizeListener  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>[IN] an instance of nsIHTMLObjectResizeListener  
</td>
</tr>

</table>

### removeObjectResizeEventListener(aListener) ###
<code>  
Deletes a resize listener  
@param aListener [IN] an instance of nsIHTMLObjectResizeListener  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>[IN] an instance of nsIHTMLObjectResizeListener  
</td>
</tr>

</table>

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
