---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIWebPageDescriptor.idl">Source file</a>
</div>

# nsIWebPageDescriptor #
<pre>  
The nsIWebPageDescriptor interface allows content being displayed in one  
window to be loaded into another window without refetching it from the  
network.  
  
</pre>
## Methods ##

### loadPage(aPageDescriptor, aDisplayType) ###
<pre>  
Tells the object to load the page specified by the page descriptor  
  
@throws NS_ERROR_FAILURE -   
  
</pre>
## Attributes ##

### currentDescriptor ###
<pre>  
Retrieves the page descriptor for the curent document.  
  
</pre>
## Constants ##

### DISPLAY_AS_SOURCE ###

### DISPLAY_NORMAL ###
