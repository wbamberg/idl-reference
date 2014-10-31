---
layout: default
---

# nsITaskbarPreviewController #
  
nsITaskbarPreviewController  
  
nsITaskbarPreviewController provides the behavior for the taskbar previews.  
Its methods and properties are used by nsITaskbarPreview. Clients are  
intended to provide their own implementation of this interface. Depending on  
the interface the controller is attached to, only certain methods/attributes  
are required to be implemented.  
  

## Methods ##

### drawPreview(ctx) ###
  
Invoked by nsITaskbarPreview when it needs to render the preview. The  
context is attached to a surface with the controller's width and height  
which are obtained immediately before the call.  
  
Note that the context is not attached to a canvas element.  
  
@param ctx Canvas drawing context  
  

#### Parameters ####

<table>

<tr>
<td>ctx</td>
<td>Canvas drawing context  
</td>
</tr>

</table>

### drawThumbnail(ctx, width, height) ###
  
Invoked by the taskbar preview when it needs to draw the thumbnail in the  
taskbar's application preview window.  
  
Note: it is guaranteed that width/height == thumbnailAspectRatio  
(modulo rounding errors)  
  
Also note that the context is not attached to a canvas element.  
  
@param ctx Canvas drawing context  
@param width The width of the surface backing the drawing context  
@param height The height of the surface backing the drawing context  
  

#### Parameters ####

<table>

<tr>
<td>ctx</td>
<td>Canvas drawing context  
</td>
</tr>

<tr>
<td>ctx</td>
<td>Canvas drawing context  
</td>
</tr>

<tr>
<td>ctx</td>
<td>Canvas drawing context  
</td>
</tr>

</table>

### onClose() ###
  
Invoked when the user presses the close button on the tab preview.  
  

### onActivate() ###
  
Invoked when the user clicks on the tab preview.  
  
@return true if the top level window corresponding to the preview should  
        be activated, false if activation is not accepted.  
  

### onClick(button) ###
  
Invoked when one of the buttons on the window preview's toolbar is pressed.  
  
@param button The button that was pressed. This can be compared with the  
              buttons returned by nsITaskbarWindowPreview.getButton.  
  

#### Parameters ####

<table>

<tr>
<td>button</td>
<td>The button that was pressed. This can be compared with the  
              buttons returned by nsITaskbarWindowPreview.getButton.  
</td>
</tr>

</table>

## Attributes ##

### width ###
  
The width of the preview image. This value is allowed to change at any  
time. See drawPreview for more information.  
  

### height ###
  
The height of the preview image. This value is allowed to change at any  
time.  See drawPreview for more information.  
  

### thumbnailAspectRatio ###
  
The aspect ratio of the thumbnail - this does not need to match the ratio  
of the preview. This value is allowed to change at any time. See  
drawThumbnail for more information.  
  
