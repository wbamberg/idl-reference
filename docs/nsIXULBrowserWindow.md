---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpfe/appshell/nsIXULBrowserWindow.idl">Source file</a>
</div>

# nsIXULBrowserWindow #
<pre>  
The nsIXULBrowserWindow supplies the methods that may be called from the  
internals of the browser area to tell the containing xul window to update  
its ui.   
  
</pre>
## Methods ##

### setJSStatus(status) ###
<pre>  
Sets the status according to JS' version of status.  
  
</pre>
### setOverLink(link, element) ###
<pre>  
Tells the object implementing this function what link we are currently  
over.  
  
</pre>
### onBeforeLinkTraversal(originalTarget, linkURI, linkNode, isAppTab) ###
<pre>  
Determines the appropriate target for a link.  
  
</pre>
### shouldLoadURI(aDocShell, aURI, aReferrer) ###
<pre>  
Determines whether a load should continue.  
  
@param aDocShell  
       The docshell performing the load.  
@param aURI  
       The URI being loaded.  
@param aReferrer  
       The referrer of the load.  
  
</pre>
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
<pre>  
Show/hide a tooltip (when the user mouses over a link, say).  
  
</pre>
### hideTooltip() ###
