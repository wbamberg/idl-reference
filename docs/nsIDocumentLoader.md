---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/base/nsIDocumentLoader.idl">Source file</a>
</div>
# nsIDocumentLoader #
  
An nsIDocumentLoader is an interface responsible for tracking groups of  
loads that belong together (images, external scripts, etc) and subdocuments  
(<iframe>, <frame>, etc). It is also responsible for sending  
nsIWebProgressListener notifications.  
XXXbz this interface should go away, we think...  
  

## Methods ##

### stop() ###

## Attributes ##

### container ###

### loadGroup ###

### documentChannel ###
