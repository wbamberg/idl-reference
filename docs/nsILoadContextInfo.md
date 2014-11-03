---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsILoadContextInfo.idl">Source file</a>
</div>

# nsILoadContextInfo #
<pre>  
Helper interface to carry informatin about the load context  
encapsulating an AppID, IsInBrowser and IsPrivite properties.  
It shall be used where nsILoadContext cannot be used or is not  
available.  
  
</pre>
## Attributes ##

### isPrivate ###
<pre>  
Whether the context is in a Private Browsing mode  
  
</pre>
### appId ###

### isInBrowserElement ###
<pre>  
Whether the context is in a browser tag  
  
</pre>
### isAnonymous ###
<pre>  
Whether the load is initiated as anonymous  
  
</pre>
## Constants ##

### NO_APP_ID ###
<pre>  
Whether the context belongs under an App  
  
</pre>
### UNKNOWN_APP_ID ###
