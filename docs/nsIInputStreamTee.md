---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIInputStreamTee.idl">Source file</a>
</div>

# nsIInputStreamTee #
  
A nsIInputStreamTee is a wrapper for an input stream, that when read  
reads the specified amount of data from its |source| and copies that  
data to its |sink|.  |sink| must be a blocking output stream.  
  

## Attributes ##

### source ###

### sink ###

### eventTarget ###
  
If |eventTarget| is set, copying to sink is done asynchronously using  
the event-target (e.g. a thread). If |eventTarget| is not set, copying  
to sink happens synchronously while reading from the source.  
  
