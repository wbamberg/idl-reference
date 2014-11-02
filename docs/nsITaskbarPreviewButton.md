---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarPreviewButton.idl">Source file</a>
</div>

# nsITaskbarPreviewButton #
  
nsITaskbarPreviewButton  
  
Provides access to a window preview's toolbar button's properties.  
  

## Attributes ##

### tooltip ###
  
The button's tooltip.  
  
Default: an empty string  
  

### dismissOnClick ###
  
True if the array of previews should be dismissed when this button is clicked.  
  
Default: false  
  

### hasBorder ###
  
True if the taskbar should draw a border around this button's image.  
  
Default: true  
  

### disabled ###
  
True if the button is disabled. This is not the same as visible.  
  
Default: false  
  

### image ###
  
The icon used for the button.  
  
Default: null  
  

### visible ###
  
True if the button is shown. Buttons that are invisible do not  
participate in the layout of buttons underneath the preview.  
  
Default: false  
  
