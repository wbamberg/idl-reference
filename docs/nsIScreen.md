---
layout: default
---

# nsIScreen #

## Methods ##

### GetRect ###

These report screen dimensions in (screen-specific) device pixels


### GetAvailRect ###

### GetRectDisplayPix ###

And these report in global display pixels


### GetAvailRectDisplayPix ###

### lockMinimumBrightness ###

Locks the minimum brightness of the screen, forcing it to be at
least as bright as a certain brightness level. Each call to this
function must eventually be followed by a corresponding call to
unlockMinimumBrightness, with the same brightness level.

@param brightness A brightness level, one of the above constants.


### unlockMinimumBrightness ###

Releases a lock on the screen brightness. This must be called
(eventually) after a corresponding call to lockMinimumBrightness.

@param brightness A brightness level, one of the above constants.


## Attributes ##

### id ###

A unique identifier for this device, useful for requerying
for it via nsIScreenManager.


### pixelDepth ###

### colorDepth ###

### rotation ###

Get/set the screen rotation, on platforms that support changing
screen rotation.


### contentsScaleFactor ###

The number of device pixels per screen point in HiDPI mode.
Returns 1.0 if HiDPI mode is disabled or unsupported.


## Constants ##

### BRIGHTNESS_DIM ###

Levels of brightness for the screen, from off to full brightness.


### BRIGHTNESS_FULL ###

### BRIGHTNESS_LEVELS ###

### ROTATION_0_DEG ###

Allowable screen rotations, when the underlying widget toolkit
supports rotating the screen.

ROTATION_0_DEG is the default, unrotated configuration.


### ROTATION_90_DEG ###

### ROTATION_180_DEG ###

### ROTATION_270_DEG ###
