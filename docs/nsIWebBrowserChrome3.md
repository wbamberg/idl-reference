---
layout: default
---

# nsIWebBrowserChrome3 #

nsIWebBrowserChrome3 is an extension to nsIWebBrowserChrome2.


## Methods ##

### onBeforeLinkTraversal ###

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


### shouldLoadURI ###

Determines whether a load should continue.

@param aDocShell
       The docshell performing the load.
@param aURI
       The URI being loaded.
@param aReferrer
       The referrer of the load.

