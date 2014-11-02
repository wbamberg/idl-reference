---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpfe/appshell/nsIXULBrowserWindow.idl">Source file</a>
</div>

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
  

#### Parameters ####

<table>

<tr>
<td>aDocShell</td>
<td>       The docshell performing the load.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>       The URI being loaded.  
</td>
</tr>

<tr>
<td>aReferrer</td>
<td>       The referrer of the load.  
</td>
</tr>

</table>

### showTooltip(x, y, tooltip) ###
  
Show/hide a tooltip (when the user mouses over a link, say).  
  

### hideTooltip() ###
