---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIIOUtil.idl">Source file</a>
</div>

# nsIIOUtil #
<pre>  
nsIIOUtil provdes various xpcom/io-related utility methods.  
  
</pre>
## Methods ##

### inputStreamIsBuffered(aStream) ###
<pre>  
Test whether an input stream is buffered.  See nsStreamUtils.h  
documentation for NS_InputStreamIsBuffered for the definition of  
"buffered" used here and for edge-case behavior.  
  
@throws NS_ERROR_INVALID_POINTER if null is passed in.  
  
</pre>
### outputStreamIsBuffered(aStream) ###
<pre>  
Test whether an output stream is buffered.  See nsStreamUtils.h  
documentation for NS_OutputStreamIsBuffered for the definition of  
"buffered" used here and for edge-case behavior.  
  
@throws NS_ERROR_INVALID_POINTER if null is passed in.  
  
</pre>