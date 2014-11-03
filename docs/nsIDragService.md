---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIDragService.idl">Source file</a>
</div>

# nsIDragService #

## Methods ##

### invokeDragSession(aDOMNode, aTransferables, aRegion, aActionType) ###
  
Starts a modal drag session with an array of transaferables   
  
@param  aTransferables - an array of transferables to be dragged  
@param  aRegion - a region containing rectangles for cursor feedback,   
           in window coordinates.  
@param  aActionType - specified which of copy/move/link are allowed  
  

#### Parameters ####

<table>

<tr>
<td>aTransferables</td>
<td>- an array of transferables to be dragged  
</td>
</tr>

<tr>
<td>aRegion</td>
<td>- a region containing rectangles for cursor feedback,   
           in window coordinates.  
</td>
</tr>

<tr>
<td>aActionType</td>
<td>- specified which of copy/move/link are allowed  
</td>
</tr>

</table>

### invokeDragSessionWithImage(aDOMNode, aTransferableArray, aRegion, aActionType, aImage, aImageX, aImageY, aDragEvent, aDataTransfer) ###
  
Starts a modal drag session using an image. The first four arguments are  
the same as invokeDragSession.  
  
A custom image may be specified using the aImage argument. If this is  
supplied, the aImageX and aImageY arguments specify the offset within  
the image where the cursor would be positioned. That is, when the image  
is drawn, it is offset up and left the amount so that the cursor appears  
at that location within the image.  
  
If aImage is null, aImageX and aImageY are not used and the image is instead  
determined from the source node aDOMNode, and the offset calculated so that  
the initial location for the image appears in the same screen position as  
where the element is located. The node must be within a document.  
  
Currently, supported images are all DOM nodes. If this is an HTML <image> or  
<canvas>, the drag image is taken from the image data. If the element is in  
a document, it will be rendered at its displayed size, othewise, it will be  
rendered at its real size. For other types of elements, the element is  
rendered into an offscreen buffer in the same manner as it is currently  
displayed. The document selection is hidden while drawing.  
  
The aDragEvent must be supplied as the current screen coordinates of the  
event are needed to calculate the image location.  
  

### invokeDragSessionWithSelection(aSelection, aTransferableArray, aActionType, aDragEvent, aDataTransfer) ###
  
Start a modal drag session using the selection as the drag image.  
The aDragEvent must be supplied as the current screen coordinates of the  
event are needed to calculate the image location.  
  

### getCurrentSession() ###
  
Returns the current Drag Session    
  

### startDragSession() ###
  
Tells the Drag Service to start a drag session. This is called when  
an external drag occurs  
  

### endDragSession(aDoneDrag) ###
  
Tells the Drag Service to end a drag session. This is called when  
an external drag occurs  
  
If aDoneDrag is true, the drag has finished, otherwise the drag has  
just left the window.  
  

### fireDragEventAtSource(aMsg) ###
  
Fire a drag event at the source of the drag  
  

### suppress() ###
  
Increase/decrease dragging suppress level by one.  
If level is greater than one, dragging is disabled.  
  

### unsuppress() ###

### dragMoved(aX, aY) ###

## Constants ##

### DRAGDROP_ACTION_NONE ###

### DRAGDROP_ACTION_COPY ###

### DRAGDROP_ACTION_MOVE ###

### DRAGDROP_ACTION_LINK ###

### DRAGDROP_ACTION_UNINITIALIZED ###
