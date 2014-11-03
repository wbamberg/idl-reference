---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/plugins/base/nsIPluginInstanceOwner.idl">Source file</a>
</div>

# nsIPluginInstanceOwner #

## Methods ##

### setInstance(aInstance) ###
<pre>  
Let the owner know what its instance is  
  
</pre>
### getInstance() ###
<pre>  
Get the instance associated with this owner.  
  
</pre>
### getWindow(aWindow) ###
<pre>  
Get a handle to the window structure of the owner.  
This pointer cannot be made persistent by the caller.  
  
</pre>
### createWidget() ###
<pre>  
Create a place for the plugin to live in the owner's  
environment. this may or may not create a window  
depending on the windowless state of the plugin instance.  
  
</pre>
### showStatus(aStatusMsg) ###
<pre>  
Show a status message in the host environment.  
  
</pre>
### invalidateRect(aRect) ###
<pre>  
Invalidate the rectangle  
  
</pre>
### invalidateRegion(aRegion) ###
<pre>  
Invalidate the region  
  
</pre>
### redrawPlugin() ###
<pre>  
Have the plugin recomposited.  
  
</pre>
### getNetscapeWindow(aValue) ###
<pre>  
Get NetscapeWindow, corresponds to NPNVnetscapeWindow  
  
</pre>
### setEventModel(eventModel) ###
<pre>  
Show native context menu  
  
</pre>
### callSetWindow() ###
<pre>  
Call NPP_SetWindow on the plugin.  
  
</pre>
### getContentsScaleFactor() ###
<pre>  
Get the contents scale factor for the screen the plugin is  
drawn on.  
  
</pre>
## Attributes ##

### mode ###
<pre>  
Get the display mode for the plugin instance.  
  
</pre>
### document ###
<pre>  
Get the associated document.  
  
</pre>