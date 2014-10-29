---
layout: default
---

# nsITaskbarWindowPreview #

## NUM_TOOLBAR_BUTTONS ##

Max 7 buttons per preview per the Windows Taskbar API


## getButton ##

Gets the nth button for the preview image. By default, all of the buttons
are invisible.

@see nsITaskbarPreviewButton

@param index The index into the button array. Must be >= 0 and <
             MAX_TOOLBAR_BUTTONS.


## enableCustomDrawing ##

Enables/disables custom drawing of thumbnails and previews

Default value: false

