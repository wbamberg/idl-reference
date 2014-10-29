---
layout: default
---

# nsIIOUtil #

nsIIOUtil provdes various xpcom/io-related utility methods.


## inputStreamIsBuffered ##

Test whether an input stream is buffered.  See nsStreamUtils.h
documentation for NS_InputStreamIsBuffered for the definition of
"buffered" used here and for edge-case behavior.

@throws NS_ERROR_INVALID_POINTER if null is passed in.


## outputStreamIsBuffered ##

Test whether an output stream is buffered.  See nsStreamUtils.h
documentation for NS_OutputStreamIsBuffered for the definition of
"buffered" used here and for edge-case behavior.

@throws NS_ERROR_INVALID_POINTER if null is passed in.

