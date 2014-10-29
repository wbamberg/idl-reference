---
layout: default
---

# nsIWebPageDescriptor #

The nsIWebPageDescriptor interface allows content being displayed in one
window to be loaded into another window without refetching it from the
network.


## DISPLAY_AS_SOURCE ##

## DISPLAY_NORMAL ##

## loadPage ##

Tells the object to load the page specified by the page descriptor

@throws NS_ERROR_FAILURE - 


## currentDescriptor ##

Retrieves the page descriptor for the curent document.

