---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITaskbarPreviewButton.idl">Source file</a>
</div>

# nsITaskbarPreviewButton #
<pre>  
nsITaskbarPreviewButton  
  
Provides access to a window preview's toolbar button's properties.  
  
</pre>
## Attributes ##

### tooltip ###
<pre>  
The button's tooltip.  
  
Default: an empty string  
  
</pre>
### dismissOnClick ###
<pre>  
True if the array of previews should be dismissed when this button is clicked.  
  
Default: false  
  
</pre>
### hasBorder ###
<pre>  
True if the taskbar should draw a border around this button's image.  
  
Default: true  
  
</pre>
### disabled ###
<pre>  
True if the button is disabled. This is not the same as visible.  
  
Default: false  
  
</pre>
### image ###
<pre>  
The icon used for the button.  
  
Default: null  
  
</pre>
### visible ###
<pre>  
True if the button is shown. Buttons that are invisible do not  
participate in the layout of buttons underneath the preview.  
  
Default: false  
  
</pre>