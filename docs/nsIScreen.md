---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIScreen.idl">Source file</a>
</div>

# nsIScreen #

## Methods ##

### GetRect(left, top, width, height) ###
<pre>  
These report screen dimensions in (screen-specific) device pixels  
  
</pre>
### GetAvailRect(left, top, width, height) ###

### GetRectDisplayPix(left, top, width, height) ###
<pre>  
And these report in global display pixels  
  
</pre>
### GetAvailRectDisplayPix(left, top, width, height) ###

### lockMinimumBrightness(brightness) ###
<pre>  
Locks the minimum brightness of the screen, forcing it to be at  
least as bright as a certain brightness level. Each call to this  
function must eventually be followed by a corresponding call to  
unlockMinimumBrightness, with the same brightness level.  
  
@param brightness A brightness level, one of the above constants.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>brightness</td>
<td>A brightness level, one of the above constants.  
</td>
</tr>

</table>

### unlockMinimumBrightness(brightness) ###
<pre>  
Releases a lock on the screen brightness. This must be called  
(eventually) after a corresponding call to lockMinimumBrightness.  
  
@param brightness A brightness level, one of the above constants.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>brightness</td>
<td>A brightness level, one of the above constants.  
</td>
</tr>

</table>

## Attributes ##

### id ###
<pre>  
A unique identifier for this device, useful for requerying  
for it via nsIScreenManager.  
  
</pre>
### pixelDepth ###

### colorDepth ###

### rotation ###
<pre>  
Get/set the screen rotation, on platforms that support changing  
screen rotation.  
  
</pre>
### contentsScaleFactor ###
<pre>  
The number of device pixels per screen point in HiDPI mode.  
Returns 1.0 if HiDPI mode is disabled or unsupported.  
  
</pre>
## Constants ##

### BRIGHTNESS_DIM ###
<pre>  
Levels of brightness for the screen, from off to full brightness.  
  
</pre>
### BRIGHTNESS_FULL ###

### BRIGHTNESS_LEVELS ###

### ROTATION_0_DEG ###
<pre>  
Allowable screen rotations, when the underlying widget toolkit  
supports rotating the screen.  
  
ROTATION_0_DEG is the default, unrotated configuration.  
  
</pre>
### ROTATION_90_DEG ###

### ROTATION_180_DEG ###

### ROTATION_270_DEG ###
