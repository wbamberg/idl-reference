---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIHTMLObjectResizer.idl">Source file</a>
</div>

# nsIHTMLObjectResizer #

## Methods ##

### showResizers(aResizedElement) ###
<pre>  
Shows active resizers around an element's frame  
@param aResizedElement [IN] a DOM Element  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aResizedElement</td>
<td>[IN] a DOM Element  
</td>
</tr>

</table>

### hideResizers() ###
<pre>  
Hide resizers if they are visible  
  
</pre>
### refreshResizers() ###
<pre>  
Refresh visible resizers  
  
</pre>
### mouseDown(aX, aY, aTarget, aMouseEvent) ###
<pre>  
event callback when a mouse button is pressed  
@param aX      [IN] horizontal position of the pointer  
@param aY      [IN] vertical position of the pointer  
@param aTarget [IN] the element triggering the event  
@param aMouseEvent [IN] the event  
  
</pre>
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
<pre>  
event callback when a mouse button is released  
@param aX      [IN] horizontal position of the pointer  
@param aY      [IN] vertical position of the pointer  
@param aTarget [IN] the element triggering the event  
  
</pre>
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
<pre>  
event callback when the mouse pointer is moved  
@param aMouseEvent [IN] the event  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aMouseEvent</td>
<td>[IN] the event  
</td>
</tr>

</table>

### addObjectResizeEventListener(aListener) ###
<pre>  
Creates a resize listener that can be used to get notifications  
that the user started to resize an object or finalized such an operation  
@param aListener [IN] an instance of nsIHTMLObjectResizeListener  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aListener</td>
<td>[IN] an instance of nsIHTMLObjectResizeListener  
</td>
</tr>

</table>

### removeObjectResizeEventListener(aListener) ###
<pre>  
Deletes a resize listener  
@param aListener [IN] an instance of nsIHTMLObjectResizeListener  
  
</pre>
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
<pre>  
the element currently displaying resizers  
  
</pre>
### objectResizingEnabled ###
<pre>  
a boolean indicating if object resizing is enabled in the editor  
  
</pre>
## Constants ##

### eTopLeft ###

### eTop ###

### eTopRight ###

### eLeft ###

### eRight ###

### eBottomLeft ###

### eBottom ###

### eBottomRight ###
