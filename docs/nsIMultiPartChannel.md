---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIMultiPartChannel.idl">Source file</a>
</div>

# nsIMultiPartChannel #
<pre>  
An interface to access the the base channel   
associated with a MultiPartChannel.  
  
</pre>
## Attributes ##

### baseChannel ###
<pre>  
readonly attribute to access the underlying channel  
  
</pre>
### partID ###
<pre>  
Attribute guaranteed to be different for different parts of  
the same multipart document.  
  
</pre>
### isLastPart ###
<pre>  
Set to true when onStopRequest is received from the base channel.  
The listener can check this from its onStopRequest to determine  
whether more data can be expected.  
  
</pre>