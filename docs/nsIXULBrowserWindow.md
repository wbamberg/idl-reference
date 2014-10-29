---
layout: default
---

# nsIXULBrowserWindow #

The nsIXULBrowserWindow supplies the methods that may be called from the
internals of the browser area to tell the containing xul window to update
its ui. 


## setJSStatus ##

Sets the status according to JS' version of status.


## setOverLink ##

Tells the object implementing this function what link we are currently
over.


## onBeforeLinkTraversal ##

Determines the appropriate target for a link.


## shouldLoadURI ##

Determines whether a load should continue.

@param aDocShell
       The docshell performing the load.
@param aURI
       The URI being loaded.
@param aReferrer
       The referrer of the load.


## showTooltip ##

Show/hide a tooltip (when the user mouses over a link, say).


## hideTooltip ##
