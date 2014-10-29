---
layout: default
---

# nsITaskbarTabPreview #

## title ##

The title displayed above the thumbnail

Default: an empty string


## icon ##

The icon displayed next to the title in the preview

Default: null


## move ##

Rearranges the preview relative to another tab preview from the same window
@param aNext The preview to the right of this one. A value of null
             indicates that the preview is the rightmost one.


## GetHWND ##

Used internally to grab the handle to the proxy window.


## EnsureRegistration ##

Used internally to ensure that the taskbar knows about this preview. If a
preview is not registered, then the API call to set its sibling (via move)
will silently fail.

This method is only invoked when it is safe to make taskbar API calls.

