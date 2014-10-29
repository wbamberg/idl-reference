---
layout: default
---

# nsIBaseWindow #

The nsIBaseWindow describes a generic window and basic operations that 
can be performed on it.  This is not to be a complete windowing interface
but rather a common set that nearly all windowed objects support.    


## Methods ##

### initWindow ###

### create ###

### destroy ###

### setPosition ###

### getPosition ###

### setSize ###

### getSize ###

### setPositionAndSize ###

### getPositionAndSize ###

### repaint ###
 
Tell the window to repaint itself
@param aForce - if true, repaint immediately
                if false, the window may defer repainting as it sees fit.


### setFocus ###

Give the window focus.


## Attributes ##

### parentWidget ###

### parentNativeWindow ###

### nativeHandle ###

### visibility ###

### enabled ###

### mainWidget ###

### unscaledDevicePixelsPerCSSPixel ###

### title ###
