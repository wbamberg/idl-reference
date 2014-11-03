---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/io/nsIUnicharOutputStream.idl">Source file</a>
</div>

# nsIUnicharOutputStream #
<pre>  
An interface that allows writing unicode data.  
  
</pre>
## Methods ##

### write(aCount, c) ###
<pre>  
Write a single character to the stream. When writing many characters,  
prefer the string-taking write method.  
  
@retval true The character was written successfully  
@retval false Not all bytes of the character could be written.  
  
</pre>
### writeString(str) ###
<pre>  
Write a string to the stream.  
  
@retval true The string was written successfully  
@retval false Not all bytes of the string could be written.  
  
</pre>
### flush() ###
<pre>  
Flush the stream. This finishes the conversion and writes any bytes that  
finish the current byte sequence.  
  
It does NOT flush the underlying stream.  
  
@see nsIUnicodeEncoder::Finish  
  
</pre>
### close() ###
<pre>  
Close the stream and free associated resources. This also closes the  
underlying stream.  
  
</pre>