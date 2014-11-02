---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIIOUtil.idl">Source file</a>
</div>
# nsIIOUtil #
  
nsIIOUtil provdes various xpcom/io-related utility methods.  
  

## Methods ##

### inputStreamIsBuffered(aStream) ###
  
Test whether an input stream is buffered.  See nsStreamUtils.h  
documentation for NS_InputStreamIsBuffered for the definition of  
"buffered" used here and for edge-case behavior.  
  
@throws NS_ERROR_INVALID_POINTER if null is passed in.  
  

### outputStreamIsBuffered(aStream) ###
  
Test whether an output stream is buffered.  See nsStreamUtils.h  
documentation for NS_OutputStreamIsBuffered for the definition of  
"buffered" used here and for edge-case behavior.  
  
@throws NS_ERROR_INVALID_POINTER if null is passed in.  
  
