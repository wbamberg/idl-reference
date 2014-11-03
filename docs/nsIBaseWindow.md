---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIBaseWindow.idl">Source file</a>
</div>

# nsIBaseWindow #
<code>  
The nsIBaseWindow describes a generic window and basic operations that   
can be performed on it.  This is not to be a complete windowing interface  
but rather a common set that nearly all windowed objects support.      
  
</code>
## Methods ##

### initWindow(parentNativeWindow, parentWidget, x, y, cx, cy) ###

### create() ###

### destroy() ###

### setPosition(x, y) ###

### getPosition(x, y) ###

### setSize(cx, cy, fRepaint) ###

### getSize(cx, cy) ###

### setPositionAndSize(x, y, cx, cy, fRepaint) ###

### getPositionAndSize(x, y, cx, cy) ###

### repaint(force) ###
<code>   
Tell the window to repaint itself  
@param aForce - if true, repaint immediately  
                if false, the window may defer repainting as it sees fit.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aForce</td>
<td>- if true, repaint immediately  
                if false, the window may defer repainting as it sees fit.  
</td>
</tr>

</table>

### setFocus() ###
<code>  
Give the window focus.  
  
</code>
## Attributes ##

### parentWidget ###

### parentNativeWindow ###

### nativeHandle ###

### visibility ###

### enabled ###

### mainWidget ###

### unscaledDevicePixelsPerCSSPixel ###

### title ###
