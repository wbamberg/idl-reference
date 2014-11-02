---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIWebBrowserChrome3.idl">Source file</a>
</div>
# nsIWebBrowserChrome3 #
  
nsIWebBrowserChrome3 is an extension to nsIWebBrowserChrome2.  
  

## Methods ##

### onBeforeLinkTraversal(originalTarget, linkURI, linkNode, isAppTab) ###
  
Determines the appropriate target for a link.  
  
@param originalTarget  
       The original link target.  
@param linkURI  
       Link destination URI.  
@param aDOMNode  
       Link DOM node.  
@param isAppTab  
       Whether or not the link is in an app tab.  
@returns A new link target, if appropriate.  
         Otherwise returns originalTarget.  
  

#### Parameters ####

<table>

<tr>
<td>originalTarget</td>
<td>       The original link target.  
</td>
</tr>

<tr>
<td>linkURI</td>
<td>       Link destination URI.  
</td>
</tr>

<tr>
<td>aDOMNode</td>
<td>       Link DOM node.  
</td>
</tr>

<tr>
<td>isAppTab</td>
<td>       Whether or not the link is in an app tab.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A new link target, if appropriate.  
         Otherwise returns originalTarget.  
</td>
</tr>

</table>

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
