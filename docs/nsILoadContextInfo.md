---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsILoadContextInfo.idl">Source file</a>
</div>
# nsILoadContextInfo #
  
Helper interface to carry informatin about the load context  
encapsulating an AppID, IsInBrowser and IsPrivite properties.  
It shall be used where nsILoadContext cannot be used or is not  
available.  
  

## Attributes ##

### isPrivate ###
  
Whether the context is in a Private Browsing mode  
  

### appId ###

### isInBrowserElement ###
  
Whether the context is in a browser tag  
  

### isAnonymous ###
  
Whether the load is initiated as anonymous  
  

## Constants ##

### NO_APP_ID ###
  
Whether the context belongs under an App  
  

### UNKNOWN_APP_ID ###
