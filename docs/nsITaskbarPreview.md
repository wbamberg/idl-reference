---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarPreview.idl">Source file</a>
</div>

# nsITaskbarPreview #
  
nsITaskbarPreview  
  
Common interface for both window and tab taskbar previews. This interface  
cannot be instantiated directly.  
  
  

## Methods ##

### invalidate() ###
  
Invalidates the taskbar's cached image of this preview, forcing a redraw  
if necessary  
  

## Attributes ##

### controller ###
  
The controller for this preview. A controller is required to provide  
the behavior and appearance of the taskbar previews. It is responsible for  
determining the size and contents of the preview, which buttons are  
displayed and how the application responds to user actions on the preview.  
  
Neither preview makes full use of the controller. See the documentation  
for nsITaskbarWindowPreview and nsITaskbarTabPreview for details on which  
controller methods are used.  
  
The controller is not allowed to be null.  
  
@see nsITaskbarPreviewController  
  

### tooltip ###
  
The tooltip displayed above the preview when the user hovers over it  
  
Default: an empty string  
  

### visible ###
  
Whether or not the preview is visible.  
  
Changing this option is expensive for tab previews since toggling this  
option will destroy/create the proxy window and its registration with the  
taskbar. If any step of that fails, an exception will be thrown.  
  
For window previews, this operation is very cheap.  
  
Default: false  
  

### active ###
  
Gets/sets whether or not the preview is marked active (selected) in the  
taskbar.  
  
