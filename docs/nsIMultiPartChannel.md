---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIMultiPartChannel.idl">Source file</a>
</div>

# nsIMultiPartChannel #
<code>  
An interface to access the the base channel   
associated with a MultiPartChannel.  
  
</code>
## Attributes ##

### baseChannel ###
  
readonly attribute to access the underlying channel  
  

### partID ###
  
Attribute guaranteed to be different for different parts of  
the same multipart document.  
  

### isLastPart ###
  
Set to true when onStopRequest is received from the base channel.  
The listener can check this from its onStopRequest to determine  
whether more data can be expected.  
  
