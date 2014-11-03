---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/plugins/base/nsIPluginInstanceOwner.idl">Source file</a>
</div>

# nsIPluginInstanceOwner #

## Methods ##

### setInstance(aInstance) ###
<code>  
Let the owner know what its instance is  
  
</code>
### getInstance() ###
<code>  
Get the instance associated with this owner.  
  
</code>
### getWindow(aWindow) ###
<code>  
Get a handle to the window structure of the owner.  
This pointer cannot be made persistent by the caller.  
  
</code>
### createWidget() ###
<code>  
Create a place for the plugin to live in the owner's  
environment. this may or may not create a window  
depending on the windowless state of the plugin instance.  
  
</code>
### showStatus(aStatusMsg) ###
<code>  
Show a status message in the host environment.  
  
</code>
### invalidateRect(aRect) ###
<code>  
Invalidate the rectangle  
  
</code>
### invalidateRegion(aRegion) ###
<code>  
Invalidate the region  
  
</code>
### redrawPlugin() ###
<code>  
Have the plugin recomposited.  
  
</code>
### getNetscapeWindow(aValue) ###
<code>  
Get NetscapeWindow, corresponds to NPNVnetscapeWindow  
  
</code>
### setEventModel(eventModel) ###
<code>  
Show native context menu  
  
</code>
### callSetWindow() ###
<code>  
Call NPP_SetWindow on the plugin.  
  
</code>
### getContentsScaleFactor() ###
<code>  
Get the contents scale factor for the screen the plugin is  
drawn on.  
  
</code>
## Attributes ##

### mode ###
  
Get the display mode for the plugin instance.  
  

### document ###
  
Get the associated document.  
  
