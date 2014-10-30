---
layout: default
---

# nsIXULBrowserWindow #
  
The nsIXULBrowserWindow supplies the methods that may be called from the  
internals of the browser area to tell the containing xul window to update  
its ui.   
  

## Methods ##

### setJSStatus(status) ###
  
Sets the status according to JS' version of status.  
  

### setOverLink(link, element) ###
  
Tells the object implementing this function what link we are currently  
over.  
  

### onBeforeLinkTraversal(originalTarget, linkURI, linkNode, isAppTab) ###
  
Determines the appropriate target for a link.  
  

### shouldLoadURI(aDocShell, aURI, aReferrer) ###
  
Determines whether a load should continue.  
  
@param aDocShell  
       The docshell performing the load.  
@param aURI  
       The URI being loaded.  
@param aReferrer  
       The referrer of the load.  
  

### showTooltip(x, y, tooltip) ###
  
Show/hide a tooltip (when the user mouses over a link, say).  
  

### hideTooltip() ###
