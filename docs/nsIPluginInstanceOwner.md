---
layout: default
---

# nsIPluginInstanceOwner #

## Methods ##

### setInstance(aInstance) ###
  
Let the owner know what its instance is  
  

### getInstance() ###
  
Get the instance associated with this owner.  
  

### getWindow(aWindow) ###
  
Get a handle to the window structure of the owner.  
This pointer cannot be made persistent by the caller.  
  

### createWidget() ###
  
Create a place for the plugin to live in the owner's  
environment. this may or may not create a window  
depending on the windowless state of the plugin instance.  
  

### showStatus(aStatusMsg) ###
  
Show a status message in the host environment.  
  

### invalidateRect(aRect) ###
  
Invalidate the rectangle  
  

### invalidateRegion(aRegion) ###
  
Invalidate the region  
  

### redrawPlugin() ###
  
Have the plugin recomposited.  
  

### getNetscapeWindow(aValue) ###
  
Get NetscapeWindow, corresponds to NPNVnetscapeWindow  
  

### setEventModel(eventModel) ###
  
Show native context menu  
  

### callSetWindow() ###
  
Call NPP_SetWindow on the plugin.  
  

### getContentsScaleFactor() ###
  
Get the contents scale factor for the screen the plugin is  
drawn on.  
  

## Attributes ##

### mode ###
  
Get the display mode for the plugin instance.  
  

### document ###
  
Get the associated document.  
  
