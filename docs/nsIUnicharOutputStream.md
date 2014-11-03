---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIUnicharOutputStream.idl">Source file</a>
</div>

# nsIUnicharOutputStream #
<code>  
An interface that allows writing unicode data.  
  
</code>
## Methods ##

### write(aCount, c) ###
<code>  
Write a single character to the stream. When writing many characters,  
prefer the string-taking write method.  
  
@retval true The character was written successfully  
@retval false Not all bytes of the character could be written.  
  
</code>
### writeString(str) ###
<code>  
Write a string to the stream.  
  
@retval true The string was written successfully  
@retval false Not all bytes of the string could be written.  
  
</code>
### flush() ###
<code>  
Flush the stream. This finishes the conversion and writes any bytes that  
finish the current byte sequence.  
  
It does NOT flush the underlying stream.  
  
@see nsIUnicodeEncoder::Finish  
  
</code>
### close() ###
<code>  
Close the stream and free associated resources. This also closes the  
underlying stream.  
  
</code>